class DominoAutomaton():

    def __init__(self, domino_input, rule="222211000222211000222100000", steps=1):
        self.domino_representation = domino_input
        self.reversed_rule = rule[::-1]
        self.steps = steps
        self.ternary_number_representation = [
            self.__bar_number_map(domino_representation_block)
            for domino_representation_block in self.domino_representation
        ]

    def time_evolution(self):
        state_vector = self.ternary_number_representation
        for _ in range(self.steps):
            state_vector = self.__new_vector(state_vector)
        return "".join(self.__number_bar_map(str(element)) for element in state_vector)

    def __new_vector(self, automaton_vector):
        _right_shifted_vector = [1] + [element for element in automaton_vector[:-1]]
        _left_shifted_vector = [element for element in automaton_vector[1:]] + [1]
        _regular_vector = automaton_vector
        return [
            self.__update_state(self.__ternary_to_decimal(tripple))
            for tripple in zip(_right_shifted_vector, _regular_vector, _left_shifted_vector)
        ]

    def __ternary_to_decimal(self, tripple):
        return tripple[0] * 3**2 + tripple[1] * 3**1 + tripple[2] * 3**0

    def __update_state(self, old_state):
        return int(self.reversed_rule[old_state])

    def __bar_number_map(self, domino_block):
        _map = {"/": 0, "|": 1, "\\": 2}
        return _map[domino_block]

    def __number_bar_map(self, ternary_domino_block_representation):
        _map = {"0": "/", "1": "|", "2": "\\"}
        return _map[ternary_domino_block_representation]
