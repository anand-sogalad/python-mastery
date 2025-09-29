from ..core.base import Operation
from ..core.registry import OperationRegistry


@OperationRegistry.register("add")
class Addition(Operation):
    def execute(self):
        return sum(self.operands)


@OperationRegistry.register("subtract")
class Subtraction(Operation):
    def execute(self):
        if len(self.operands) < 2:
            raise ValueError("Subtraction requires at least 2 operands")
        result = self.operands[0]
        for operand in self.operands[1:]:
            result -= operand
        return result


@OperationRegistry.register("multiply")
class Multiplication(Operation):
    def execute(self):
        result = 1
        for operand in self.operands:
            result *= operand
        return result


@OperationRegistry.register("divide")
class Division(Operation):
    def execute(self):
        if len(self.operands) != 2:
            raise ValueError("Division requires exactly 2 operands")
        dividend, divisor = self.operands
        if divisor == 0:
            raise ZeroDivisionError("Division by zero")
        return dividend / divisor
