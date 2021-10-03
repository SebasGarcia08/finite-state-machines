from fsm import FSM


def read_line(reader) -> str:
    return reader.readline().strip()


def solve(input_file: str):
    reader = open(input_file, "r")
    num_tests = int(read_line(reader))
    for t in range(num_tests):
        machine_type = int(read_line(reader))
        S = read_line(reader).split()
        R = read_line(reader).split()
        Q = read_line(reader).split()
        init_state = Q[0]

        S, Q, R = map(tuple, [S, Q, R])
        fsm = FSM(S, R, Q, init_state)

        for _ in range(len(Q)):
            row = read_line(reader).split()
            state = row[0]
            i = 1
            while i < 2*len(S) + 1:
                transitions = []
                for _ in range(len(S)):
                    transitions.append((row[i], row[i+1]))
                    i += len(S)
                fsm.add_transitions(state, transitions)
        partitioned_states = fsm.partition(verbose=False)
        print(len(partitioned_states))
        for i, block in enumerate(partitioned_states):
            print(*block)


if __name__ == '__main__':
    solve("../test_input.txt")
