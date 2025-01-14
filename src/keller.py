class Stack:

    def __init__(self, stack_alphabet: list, initial_symbol: str):
        self._alphabet = stack_alphabet
        self._stack = [initial_symbol]
        self.stack_length = 1

    def stack_push(self, symbol):
        if symbol in self._alphabet:
            self._stack.append(symbol)
            self.stack_length = len(self._stack)
        else:
            raise ValueError(f"{self._alphabet}", f"Got {symbol}, expected")

    def stack_pop(self):
        popped = self._stack.pop()
        self.stack_length = len(self._stack)
        return popped