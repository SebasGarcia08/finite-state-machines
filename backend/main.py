from fsm import FSM
from typing import List, Callable, Dict, Tuple
from pprint import pprint


def parse_transition_table(fsm: FSM, transition_table: List[str], machine_type: str) -> None:
    S = fsm.S
    conditions: Dict[str, Callable[[int], bool]] = {
        'T': lambda idx: idx < 2 * len(S) + 1,
        'S': lambda idx: idx < len(S) + 1
    }

    get_transitions: Dict[str, Callable[[List[str], int], Tuple[str, str]]] = {
        'T': lambda tt_row, idx: (tt_row[idx], tt_row[idx + 1]),
        'S': lambda tt_row, idx: (tt_row[idx], tt_row[-1])
    }

    step_rule: Dict[str, Callable[[int], int]] = {
        'T': lambda idx: idx + len(S),
        'S': lambda idx: idx + 1
    }

    condition = conditions[machine_type]
    get_transition = get_transitions[machine_type]
    step = step_rule[machine_type]

    for row in transition_table:
        row_split: List[str] = row.split()
        state = row_split[0]
        i = 1
        while condition(i):
            transitions = []
            for _ in range(len(S)):
                transition = get_transition(row_split, i)
                transitions.append(transition)
                i = step(i)
            fsm.add_transitions(state, transitions)


def solve_test_case(input_test_case: List[str]) -> Tuple[FSM, int]:
    """Parses a single test case
    Args:
        input_test_case(List[str]): List of strings containing remaining cases
    Return:
        inaccessible_states(List[str]): inaccessible states of the FSM
        partitioned_states(List[List[str]]): blocks conforming the final partition of the FSM
        next_test_case_index(int): the number of lines that this test case took: 5 + |Q| + 1
    """
    machine_type: str = input_test_case[0]
    S = input_test_case[1].split()
    R = input_test_case[2].split()
    Q = input_test_case[3].split()
    init_state = Q[0]

    S, Q, R = map(tuple, [S, Q, R])
    fsm = FSM(S=S, R=R, Q=Q, init_state=init_state)
    end_test_case = 4 + len(Q)
    transition_table = input_test_case[4: end_test_case]
    parse_transition_table(fsm, transition_table, machine_type)
    next_test_case_index = end_test_case
    return fsm, next_test_case_index


def solve(lines: List[str]) -> List[Tuple[FSM, FSM]]:
    solutions = []
    num_tests = int(lines[0])
    test_cases_index = 1
    for t in range(num_tests):
        test_case_input = lines[test_cases_index:]
        fsm, next_test_case_index = solve_test_case(test_case_input)
        print(f"FSM: \n{fsm = }")
        print()
        print(f"Minimum equivalent: \n{fsm.minimum_equivalent()}")
        solutions.append((fsm, fsm.minimum_equivalent()))
        test_cases_index += next_test_case_index
        print()
    return solutions


if __name__ == '__main__':
    with open("../test_input.txt", 'r') as f:
        l = list(map(lambda s: s.strip(), f.readlines()))
    print(l)
    solve(l)
# solve("../test_input.txt")
