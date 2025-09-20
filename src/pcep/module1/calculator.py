"""
lab1:
Implement Simple arthimetic calulator
Use Objec Oriented skills
"""


class CalculatorDecorator:
    """
    A decorator class for calculator operations to handle invalid inputs and exceptions.
    Methods
    -------
    invalid_operation(func):
        Static method decorator that checks for string inputs and handles TypeError and ZeroDivisionError,
        returning appropriate error messages.
    """

    @staticmethod
    def invalid_operation(func):
        def wrapper(num1, num2):
            if isinstance(num1, str) or isinstance(num2, str):
                return "Invalid operation! alteast a variable is str"
            try:
                return func(num1, num2)
            except TypeError:
                return f"Invalid operation! {func.__name__} not supported between {type(num1)} and {type(num2)} operators by calculator"
            except ZeroDivisionError:
                return f"ZeroDivisionError! {func.__name__} not supported when num2 is {num2}"

        return wrapper


class Calculator:
    """
    Calculator class providing basic arithmetic operations as static methods.
    All methods are decorated to handle invalid operations.
    """

    @staticmethod
    @CalculatorDecorator.invalid_operation
    def addition(num1, num2):
        return num1 + num2

    @staticmethod
    @CalculatorDecorator.invalid_operation
    def subtraction(num1, num2):
        return num1 - num2

    @staticmethod
    @CalculatorDecorator.invalid_operation
    def multiplication(num1, num2):
        return num1 * num2

    @staticmethod
    @CalculatorDecorator.invalid_operation
    def division(num1, num2):
        return num1 / num2

    @staticmethod
    @CalculatorDecorator.invalid_operation
    def floor_division(num1, num2):
        return num1 // num2

    @staticmethod
    @CalculatorDecorator.invalid_operation
    def exponention(num1, num2):
        return num1**num2
