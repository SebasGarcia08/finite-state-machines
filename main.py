from fsm import FSM


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
        print(fsm._transitions)
        print(fsm.partition())


if __name__ == '__main__':
    solve("test_input.txt")
