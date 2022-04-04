from sys import argv
from domino_automaton import DominoAutomaton


def main():
    args = argv[1:]
    print(args)
    input = args[0]
    steps = int(args[1])
    time_forward = bool(int(args[2])) if len(args) == 3 else True
    automaton = DominoAutomaton(input, steps=steps, time_forward=time_forward)
    print("final state:\t", automaton.time_evolution())


if __name__ == "__main__":
    main()
