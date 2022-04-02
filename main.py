from sys import argv
from domino_automaton import DominoAutomaton


def main():
    args = argv[1:]
    print(args)
    input = args[0]
    steps = int(args[1])
    automaton = DominoAutomaton(input, steps=steps)
    print("initial state:\t", automaton.domino_representation)
    print("final state:\t", automaton.time_evolution())


if __name__ == "__main__":
    main()
