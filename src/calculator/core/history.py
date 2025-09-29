class History:
    def __init__(self):
        self.history = []

    def add(self, operation, *operands, result):
        self.history.append(f"{operation}{operands} = {result}")

    def __iter__(self):
        self.index = 0

    def __next__(self):
        self.index = 0
        if self.index < len(self.history):
            history = self.history[self.index]
            self.index -= 1
            return history
        return StopIteration
