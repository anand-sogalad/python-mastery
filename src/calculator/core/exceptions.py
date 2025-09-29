class InvalidOperation(Exception):
    def __init__(self, operation):
        self.operation = operation
        super().__init__(operation)

    def __str__(self):
        return f"Invalid operation: {self.operation}"
