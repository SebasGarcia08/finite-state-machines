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
    S: Tuple
    R: Tuple
    Q: Tuple
    init_state: str
    _transitions: List[List[Tuple[int, int]]] = field(default_factory=list)
    _inaccessible_states: List[str] = None

    def __post_init__(self) -> None:
        for _ in range(len(self.Q)):
            self._transitions.append([None] * len(self.S))

    @property
    def inaccessible_states(self) -> List[str]:
        if self._inaccessible_states is None:
            self._inaccessible_states = self._get_inaccessible_states()
        return self._inaccessible_states

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
        initial_partition: List[Set[str]] = []
        pass

    def _partition(self, prev_partition: List[Set[str]]):
        pass

    def _get_inaccessible_states(self) -> List[str]:
        start_idx = self.Q.index(self.init_state)
        accessible_states_idxs: Set[int] = set()
        self._get_accessible_states_from(start_idx, accessible_states_idxs)
        inaccessible_states_idxs = set(range(len(self.Q))) - accessible_states_idxs
        inaccessible_states = list(map(lambda idx: self.Q[idx], inaccessible_states_idxs))
        return inaccessible_states

    def _get_accessible_states_from(self, src_idx: int, visited: Set[int]) -> None:
        to_visit = set(map(lambda x: x[0], self._transitions[src_idx]))
        visited.add(src_idx)
        #print(f"{visited = }")
        #print(f"{ to_visit = }")
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


def read_line(reader) -> str:
    return reader.readline().strip()


def solve(input_file: str):
    reader = open(input_file, "r")
    num_tests = int(read_line(reader))
    for t in range(num_tests):
        len_s = int(read_line(reader))
        S = read_line(reader).split()
        len_r = int(read_line(reader))
        R = read_line(reader).split()
        len_q = int(read_line(reader))
        Q = read_line(reader).split()
        init_state = read_line(reader)

        S, Q, R = map(tuple, [S, Q, R])
        fsm = FSM(S, R, Q, init_state)

        for _ in range(len_q):
            row = read_line(reader).split()
            state = row[0]
            i = 1
            while i < 2*len_s + 1:
                transitions = []
                for _ in range(len_s):
                    transitions.append((row[i], row[i+1]))
                    i += len_s
                fsm.add_transitions(state, transitions)
        print(fsm)
        print(fsm.inaccessible_states)


def mini_test():
    automata = {
        "S": ["a", "b"],
        "Q": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        "R": ["0", "1", "2", "3"],
        "init_state": 0,
        "_transitions": [
            ((1, 1), (2, 2)),  # "A": [("B", "1"), ("C",  "2")]
            ((2, 2), (3, 3)),  # "B": [("C", "2"), ("D", "3")]
            ((3, 3), (0, 0)),
            ((0, 0), (1, 1))
        ]
    }

    fsm = FSM(
        S=("a", "b"),
        Q=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'),
        R=("0", "1", "2", "3"),
        init_state="A"
    )
    fsm.add_transitions(state='C', transitions=[('D', '3'), ('A', '0')])
    print(fsm)
    print(fsm._transitions)


if __name__ == '__main__':
    solve("test_input.txt")
