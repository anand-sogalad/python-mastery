from .core.history import History
from .core.registry import OperationRegistry

# Import operations to trigger the decorators
from .operations import arithmetic


class Calculator:
    def __init__(self):
        self.history = History()
        self.registry = OperationRegistry()

    def run_operation(self, operation, *operands):
        op_cls = self.registry.get(operation)
        if op_cls is None:
            raise KeyError(
                f"Operation '{operation}' not found. Available operations: {list(self.registry.get_registry().keys())}"
            )
        result = op_cls(*operands).execute()
        self.history.add(operation, *operands, result=result)
        return result
