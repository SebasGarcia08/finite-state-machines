from typing import List, Tuple, Set, Dict, Any, NamedTuple, Union, Iterator
from argparse import ArgumentParser
from dataclasses import dataclass
import logging
import re

logging.basicConfig(
    filename="log_file_name.log",
    level=logging.INFO,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)

logger = logging.getLogger(__name__)
EMPTY_SET: Set[Any] = set()


class ParsingError(Exception):
    pass


class Symbol(object):
    def __init__(self, name: str):
        self.name = name
        if len(self.name) != 1:
            raise ValueError(f"Symbol name must be 1 character long, got {self.name}")

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Symbol):
            return self.name == o.name
        if isinstance(o, str):
            return self.name == o
        return False

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)


class Variable(Symbol):
    def __init__(self, name: str):
        super().__init__(name)
        if self.name.isalpha() and not self.name.isupper():
            logger.debug("Variable should be uppercase, got {self.name}")


class Terminal(Symbol):
    def __init__(self, name: str):
        super().__init__(name)
        if self.name.isalpha() and not self.name.isupper():
            logger.debug("Terminal should be lowercase, got {self.name}")


Production = Tuple[Union[Terminal, Variable], ...]
ProcessTable = List[List[Set[Variable]]]
InputString = List[Production]


@dataclass
class Grammar:
    start: Variable
    variables: Set[Variable]
    terminals: Set[Terminal]
    productions: Dict[Variable, Set[Production]]


class Answer(NamedTuple):
    """Class defining the format of the answer
    and process to determine wheter
    the string is produced by the grammar
    using the CYK algorithm.

    Arguments:
        string (str): string to be checked.
        grammar: Grammar: grammar to be used.
        answer (bool): True if the string is produced by the grammar.
        table (List[List[Union[Set[Variable], None]]]): CYK table
    Usage:
    ??????
    string = ["b","a","a","b","a"]
    grammar = Grammar(
        start="S",
        variables={
            Variable("S"),
            Variable("A"),
            Variable("B"),
            Variable("C")
        },
        terminals={Terminal("a"), Terminal("b")},
        productions={
            "S": {
                ["A", "B"],
                ["B", "C"]
            },
            "A": {
                ["B","A"],
                ["a"]
            },
            "B": {
                ["C","C"],
                ["b"]
            },
            "C": {
                ["A","B"],
                ["a"]
            }
        },
        result=True,
        table=[
            [
                "b",
                "a",
                "a",
                "b",
                "a"
            ],
            [
                {"B"},
                {"A", "C"},
                {"A","C"},
                {"B"},
                {"A","C"}
            ],
            [
                {"S", "A"},
                {"B"},
                {"S", "C"},
                {"S","A"}
            ],
            [
                {None},
                {"B"},
                {"B"}
            ],
            [
                {None},
                {"S", "A", "C"}
            ],
            [
                {"S", "A", "C"}
            ],
        ]
    )
    ??????
    """

    string: InputString
    grammar: Grammar
    result: bool
    table: ProcessTable
    explanation: str


def initialize_table(string: InputString, G: Grammar) -> ProcessTable:
    table: ProcessTable = list()

    # Initialize table
    for i in range(len(string)):
        ith_row: List[Set[Variable]] = [set() for _ in range(len(string) - i)]
        table.append(ith_row)

    # Fill first row of table with variables that produce each terminal
    for i in range(len(string)):
        for s in string[i : i + 1]:
            for variable, productions in G.productions.items():
                for production in productions:
                    if s == production:
                        table[0][i].add(variable)
    return table


def cartesian_product_productions(
    left_prod: Set[Variable], right_prod: Set[Variable]
) -> Iterator[Production]:
    for l in left_prod:
        for r in right_prod:
            yield (
                l,
                r,
            )


def prod2str(p: List[Production]) -> str:
    return "".join(str(x[0]) for x in p)


def solve(G: Grammar, string: InputString) -> Answer:
    table = initialize_table(string, G)
    explanation = ""

    # Fill the rest of the table, start from 2 because we already filled the first row
    for j in range(2, len(string) + 1):
        for i in range(len(string) - j + 1):
            substring = string[i : i + j]
            explanation += f"i = {i}, j = {j}, {prod2str(substring)}\n"
            for k in range(1, j):
                left, right = substring[:k], substring[k:]
                left_prod = table[len(left) - 1][i]
                right_prod = table[len(right) - 1][i + len(substring) - len(right)]
                explanation += f"\tk = {k}, \n\t{prod2str(left)}: {left_prod}, \n\t{prod2str(right)}: {right_prod}\n"

                if left_prod == EMPTY_SET or right_prod == EMPTY_SET:
                    explanation += f"\tSkipping since none produces left or right\n"
                    explanation += "\n"
                    continue

                cartesian_product = cartesian_product_productions(left_prod, right_prod)
                for candidate_production in cartesian_product:
                    for variable, productions in G.productions.items():
                        for production in productions:
                            if candidate_production == production:
                                explanation += f"\tAdding {variable} because produces {''.join(str(s) for s in candidate_production)}\n"
                                table[j - 1][i].add(variable)
                explanation += "\n"
        explanation += "\n"
    result = G.start in table[-1][0]
    ans = Answer(string, G, result, table, explanation)
    return ans


def del_extra_spaces(string: str) -> str:
    return re.sub(" +", " ", string)


def parse_productions(
    lines: List[str], variables: Set[Variable], terminals: Set[Terminal]
) -> Dict[Variable, Set[Production]]:
    productions: Dict[Variable, Set[Production]] = dict()
    for line_prod in lines:
        raw_production = line_prod.strip().split("->")
        variable = Variable(raw_production[0].strip())
        if not productions.get(variable):
            productions[variable] = set()
        product = list(map(str.strip, raw_production[1].split("|")))
        for prod in product:
            single_production: List[Union[Terminal, Variable]] = list()
            for s in prod:
                if s in variables:
                    single_production.append(Variable(s))
                elif s in terminals:
                    single_production.append(Terminal(s))
                else:
                    raise ParsingError(f"Unknown symbol {s} in production {prod}")
            production = tuple(single_production)
            productions[variable].add(production)
    return productions


def parse_input(lines: List[str], n: int) -> Iterator[Tuple[Grammar, InputString]]:
    """
    Parse input file.
    :param input_file: input file name
    :return: parsed input
    """
    i = 0
    for _ in range(n):
        string: InputString = list(map(lambda x: (Terminal(x),), lines[i].strip()))
        start_var: Variable = Variable(lines[i + 1])
        variables: Set[Variable] = set(map(Variable, lines[i + 2].strip().split()))
        terminals: Set[Terminal] = set(map(Terminal, lines[i + 3].strip().split()))
        start = i + 4
        stop = start + len(variables)
        productions = parse_productions(lines[start:stop], variables, terminals)

        G = Grammar(
            start=start_var,
            variables=variables,
            terminals=terminals,
            productions=productions,
        )
        i = i + stop
        yield G, string


def main(args: Dict[str, Any]) -> List[Answer]:
    with open(args["input_file"], "r") as f:
        lines = f.read().split("\n")
    n = int(lines[0])
    lines = list(map(del_extra_spaces, lines[1:]))
    answers: List[Answer] = list()
    for G, string in parse_input(lines, n):
        ans = solve(G, string)
        answers.append(ans)
        print(ans.explanation)
        for r in ans.table:
            print(r)
    return answers


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-i", "--input-file", help="input file name", type=str, default="cyk_input.txt",
    )
    parser.add_argument(
        "-o" "--output-file",
        help="output file name",
        type=str,
        default="cyk_output.txt",
    )
    args = parser.parse_args()
    main(vars(args))
