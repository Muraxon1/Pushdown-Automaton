from keller import Stack


class Automata:
    def __init__(self, state_set, input_alphabet, stack_alphabet, transition_relations,
                 start_state, initial_stack_symbol, accepting_states):
        self._state_set = state_set
        self._input_alphabet = input_alphabet
        self._stack_alphabet = stack_alphabet

        # validate transition relations
        self._transition_relations = transition_relations

        # validate start state
        if start_state in state_set:
            self._start_state = start_state
        else:
            raise ValueError(f"Start state '{start_state}' not in state set: {state_set}")

        # validate initial stac symbol
        if initial_stack_symbol in stack_alphabet:
            self._initial_stack_symbol = initial_stack_symbol
        else:
            raise ValueError(f"Initial stack symbol '{initial_stack_symbol}' not in stack alphabet: {stack_alphabet}")

        # validate starting states
        if accepting_states in state_set:
            self._accepting_states = accepting_states
        else:
            raise ValueError(f"accepting states: '{accepting_states}' not in state set: {state_set}")
        
        self._stack = Stack(self._stack_alphabet, self._initial_stack_symbol)

