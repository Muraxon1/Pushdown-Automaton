class StackSymbolError(Exception):
    def __init__(self, input_value, message="Invalid input provided"):
        self.input_value = input_value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.input_value}"