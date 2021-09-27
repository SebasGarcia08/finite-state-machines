from mimetypes import init

import _io
from typing import List, Dict, Set, Union
from typing import Tuple
from dataclasses import dataclass, field


@dataclass
class FSM:
    """Finite State Machine
    Args:
      S (Tuple[str]): the input alphabet
      R (Tuple[str]): the output alphabet
      Q (Tuple[str]): the set of states
      init_state (str): the initial state
    """
    S: Tuple[str, ...]
    R: Tuple[str, ...]
    Q: Tuple[str, ...]
    init_state: str
    _transitions: List[List[Tuple[int, int]]] = field(default_factory=list)
    _inaccessible_states: List[int] = None

    def __post_init__(self) -> None:
        for i in range(len(self.Q)):
            self._transitions.append([None] * len(self.S))

    @property
    def inaccessible_states(self) -> List[str]:
        if self._inaccessible_states is None:
            self._inaccessible_states = self._get_inaccessible_states()
        inaccessible_states = list(map(lambda idx: self.Q[idx], self._inaccessible_states))
        return inaccessible_states

    def add_transition(self, src: str, dest: str, stimulus: str, output: str) -> None:
        """
        Adds the connection of a state
        """
        src_state_idx = self.Q.index(src)
        dest_state_idx = self.Q.index(dest)
        out_idx = self.R.index(output)
        stimulus_idx = self.S.index(stimulus)
        self._transitions[src_state_idx][stimulus_idx] = (dest_state_idx, out_idx)

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

    def partition(self):
        initial_partition: List[List[int]] = []
        possible_outs: Dict[Tuple, Set[int]] = dict()
        self._inaccessible_states = self._get_inaccessible_states()
        print(f"{self._inaccessible_states = }")
        for i in range(len(self._transitions)):
            if i in self._inaccessible_states:
                continue
            outs = tuple(map(lambda x: x[1], self._transitions[i]))
            if outs not in possible_outs:
                possible_outs[outs] = {i}
            else:
                possible_outs[outs].add(i)
        for block in possible_outs.values():
            initial_partition.append(list(block))
            print(list(map(lambda idx: self.Q[idx], block)))
        print(f"{initial_partition = }")
        self._partition(initial_partition)

    def _get_successors(self, partition: List[List[int]]) -> List[List[Tuple]]:
        block_s_successors: List[List[Tuple]] = []
        for block in partition:
            block_successors: List[Tuple] = []
            for state in block:
                state_successors = tuple(self._transitions[state][i][0]
                                         for i in range(len(self.S)))
                block_successors.append(state_successors)
            block_s_successors.append(block_successors)
        return block_s_successors

    def _partition(self, prev_partition: List[List[int]]):
        block_s_successors = self._get_successors(prev_partition)
        for successors_block in block_s_successors:
            print(successors_block)
            for block in successors_block:
                print(tuple(map(lambda idx: self.Q[idx], block)), end=" ")

        new_partition: Dict[Tuple, int] = dict()
        for i_block in range(len(prev_partition)):
            for i_successors in range(len(block_s_successors[i_block])):
                s_successors = block_s_successors[i_block][i_successors]
                prev_block_belongs = tuple(self._which_block(s, prev_partition) for s in s_successors)
                #print(prev_partition[i_block][i_successors], prev_block_belongs)
                #print()
        print()

    def _which_block(self, successor: int, partition: List[List[int]]) -> int:
        for i, block in enumerate(partition):
            if successor in block:
                return i

    def _get_inaccessible_states(self) -> List[int]:
        start_idx = self.Q.index(self.init_state)
        accessible_states_idxs: Set[int] = set()
        self._get_accessible_states_from(start_idx, accessible_states_idxs)
        inaccessible_states_idxs = list(set(range(len(self.Q))) - accessible_states_idxs)
        return inaccessible_states_idxs

    def _get_accessible_states_from(self, src_idx: int, visited: Set[int]) -> None:
        to_visit = set(map(lambda x: x[0], self._transitions[src_idx]))
        visited.add(src_idx)
        for to_vis in to_visit:
            if to_vis not in visited:
                self._get_accessible_states_from(to_vis, visited)

    def __repr__(self) -> str:
        string = ""
        names = ["states", "input alphabet", "output alphabet"]
        objs = [self.Q, self.S, self.R]

        for name, obj in zip(names, objs):
            string += f"{name} = {obj} \n"
        string += f"Initial state = {self.init_state} \n"
        string += "Transition table: \n"
        string += "Q\t" + "\t".join(f"S={s} " for s in self.S) + "\n"

        for i, t in enumerate(self._transitions):
            if all(x is not None for x in t):
                string += f"{self.Q[i]}\t"
                for dest_state_idx, out_idx in t:
                    string += f"{self.Q[dest_state_idx]}, {self.R[out_idx]}\t"
                string += "\n"
        return string

