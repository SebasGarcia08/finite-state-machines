from typing import List, Dict, Set, Union
from typing import Tuple
from dataclasses import dataclass, field
from pprint import pprint
from copy import deepcopy


@dataclass
class FSM:
    S: Tuple[str, ...]
    R: Tuple[str, ...]
    Q: Tuple[str, ...]
    init_state: str
    _transitions: Dict[str, Dict[str, Tuple[str, str]]] = field(default_factory=dict)
    _inaccessible_states: List[str] = None
    _partitions: List[List[List[str]]] = None
    """Finite State Machine
    Args:
      S (Tuple[str]): the input alphabet
      R (Tuple[str]): the output alphabet
      Q (Tuple[str]): the set of states
      init_state (str): the initial state
    """

    def __post_init__(self) -> None:
        for q in self.Q:
            self._transitions[q] = dict()

    @property
    def inaccessible_states(self) -> List[str]:
        if self._inaccessible_states is None:
            self._inaccessible_states = self._get_inaccessible_states()
        return self._inaccessible_states

    @property
    def partitions(self) -> List[List[List[str]]]:
        if self._partitions is None:
            self._partitions = self._partition()
        return self._partitions

    @property
    def blocks(self) -> List[List[str]]:
        return self.partitions[-1]

    def _check_valid_transition(self, src: str, dest: str, stimulus: str, output: str):
        results = {
            'source state': (src, self.Q),
            'destiny state': (dest, self.Q),
            'stimulus': (stimulus, self.S),
            'output': (output, self.R)
        }
        msg = ""
        valid_inputs: List[bool] = []
        for name, (received, possible_values) in results.items():
            valid = received in possible_values
            if not valid:
                msg += f'{name} {received} not found in any of {possible_values}'
            valid_inputs.append(valid)

        if not all(valid_inputs):
            raise KeyError(msg)

    def add_transition(self, src: str, dest: str, stimulus: str, output: str) -> None:
        """
        Adds the connection of a state
        """
        self._check_valid_transition(src, dest, stimulus, output)
        self._transitions[src][stimulus] = (dest, output)

    def add_transitions(
            self,
            state: str,
            transitions: Union[
                Dict[str, Tuple[str, str]],
                List[Tuple[str, str]]
            ]
    ):
        iterable = transitions.items() if type(transitions) == dict else enumerate(transitions)
        for s, t in iterable:
            stimulus = self.S[s] if type(transitions) == list else s
            dest_state, output = t
            self.add_transition(src=state, dest=dest_state, stimulus=stimulus, output=output)

    def connected(self) -> 'FSM':
        inaccessible_states = self._get_inaccessible_states()
        accessible_states = list(self.Q)
        connected_transitions = self._transitions.copy()
        for x in inaccessible_states:
            accessible_states.remove(x)
            del (connected_transitions[x])
        connected_fsm = FSM(Q=tuple(accessible_states), S=self.S, R=self.R, init_state=self.init_state)
        connected_fsm._transitions = connected_transitions
        return connected_fsm

    def minimum_equivalent(self) -> 'FSM':
        blocks = self.blocks
        inaccessible_states = self.inaccessible_states
        state_2_equivalent: Dict[str, str] = dict()
        equivalent_Q = []
        for i, block in enumerate(blocks):
            equivalent_state = f'q{i+1}'
            for state_2_replace in block:
                state_2_equivalent[state_2_replace] = equivalent_state
            equivalent_Q.append(equivalent_state)

        equivalent_Q = tuple(equivalent_Q)
        equivalent_transitions: Dict[str, Dict[str, Tuple[str, str]]] = deepcopy(self._transitions)
        old_transitions_keys = list(equivalent_transitions.keys())
        for old_state in old_transitions_keys:
            if old_state in inaccessible_states:
                continue
            transitions_2_map = equivalent_transitions[old_state]
            for stimulus in transitions_2_map.keys():
                old_transition = transitions_2_map[stimulus]
                dest_state, output = old_transition
                transitions_2_map[stimulus] = (state_2_equivalent[dest_state], output)
            renamed_state = state_2_equivalent[old_state]
            equivalent_transitions[renamed_state] = transitions_2_map
        pprint(state_2_equivalent)
        keys = list(equivalent_transitions.keys())
        for k in keys:
            if not k.startswith('q'):
                del equivalent_transitions[k]
        equivalent_initial_state = state_2_equivalent[self.init_state]
        minimum_equivalent_fsm = FSM(
            Q=equivalent_Q,
            R=self.R,
            S=self.S,
            init_state=equivalent_initial_state
        )
        minimum_equivalent_fsm._transitions = equivalent_transitions
        return minimum_equivalent_fsm

    def _partition(self, verbose: bool = False) -> List[List[List[str]]]:
        initial_partition: List[List[str]] = []
        possible_outs: Dict[Tuple, Set[str]] = dict()
        self._inaccessible_states = self._get_inaccessible_states()
        for i in self._transitions.keys():
            if i in self._inaccessible_states:
                continue
            outs = tuple(map(lambda x: x[1], self._transitions[i].values()))
            if outs not in possible_outs:
                possible_outs[outs] = {i}
            else:
                possible_outs[outs].add(i)
        for block in possible_outs.values():
            initial_partition.append(list(block))
        if verbose:
            print(initial_partition)
        partitions = [list(self.Q), initial_partition]
        return self._recursive_partition(partitions=partitions, verbose=verbose)

    def _get_successors(self, partition: List[List[str]]) -> List[List[Tuple]]:
        block_s_successors: List[List[Tuple]] = []
        for block in partition:
            block_successors: List[Tuple] = []
            for state in block:
                state_successors = tuple(self._transitions[state][s][0]
                                         for s in self.S)
                block_successors.append(state_successors)
            block_s_successors.append(block_successors)
        return block_s_successors

    def _recursive_partition(self, partitions: List[List[List[str]]], verbose: bool = False) -> List[List[List[str]]]:
        prev_partition = partitions[-1]
        block_s_successors = self._get_successors(prev_partition)

        new_partition_buckets: Dict[Tuple[int, Tuple[int, ...]], List[str]] = dict()
        for i_block in range(len(prev_partition)):
            for i_successors in range(len(block_s_successors[i_block])):
                s_successors = block_s_successors[i_block][i_successors]
                # Add as prefix the block in order to differentiate
                prev_block_belongs = (i_block, tuple(self._which_block(s, prev_partition)
                                                     for s in s_successors)
                                      )
                state_belongs = prev_partition[i_block][i_successors]
                if prev_block_belongs not in new_partition_buckets:
                    new_partition_buckets[prev_block_belongs] = [state_belongs]
                else:
                    new_partition_buckets[prev_block_belongs].append(state_belongs)

        new_partition: List[List[str]] = list(new_partition_buckets.values())
        if verbose:
            print(new_partition)
        if new_partition == prev_partition:
            return partitions
        else:
            partitions.append(new_partition)
            return self._recursive_partition(partitions)

    @staticmethod
    def _which_block(successor: int, partition: List[List[str]]) -> int:
        for i, block in enumerate(partition):
            if successor in block:
                return i

    def _get_inaccessible_states(self) -> List[str]:
        accessible_states: Set[str] = set()
        self._get_accessible_states_from(self.init_state, accessible_states)
        inaccessible_states = list(set(self.Q) - accessible_states)
        return inaccessible_states

    def _get_accessible_states_from(self, src: str, visited: Set[str]) -> None:
        to_visit = set(map(lambda x: x[0], self._transitions[src].values()))
        visited.add(src)
        for to_vis in to_visit:
            if to_vis not in visited:
                self._get_accessible_states_from(to_vis, visited)

    def __repr__(self) -> str:
        string = ""
        names = ["states", "input alphabet", "output alphabet"]
        objs = [self.Q, self.S, self.R]

        for name, obj in zip(names, objs):
            string += f"{name} = {obj} \n"
        string += f"Initial state = {self.init_state} \n\n"
        string += "Transition table: \n"
        string += "Q\t" + "\t".join(f"S={s} " for s in self.S) + "\n"

        for q, t in self._transitions.items():
            if all(x is not None for x in t):
                string += f"{q}\t"
                for dest_state, output in t.items():
                    string += f"{output[0]}, {output[1]}\t"
                string += "\n"
        string += f'Inaccessible states: {self.inaccessible_states}\n'
        string += "Partitions: \n"
        for i, p in enumerate(self.partitions):
            string += f"p{i}: {p}\n"
        return string
