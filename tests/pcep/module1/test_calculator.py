from src.pcep.module1.calculator import Calculator


class TestCalculator:
    def test_addition_basic(self):
        assert Calculator.addition(2, 3) == 5

    def test_subtraction_basic(self):
        assert Calculator.subtraction(5, 2) == 3

    def test_multiplication_basic(self):
        assert Calculator.multiplication(4, 3) == 12

    def test_division_basic(self):
        assert Calculator.division(10, 2) == 5

    def test_floor_division_basic(self):
        assert Calculator.floor_division(9, 2) == 4

    def test_exponention_basic(self):
        assert Calculator.exponention(2, 3) == 8

    def test_addition_with_string(self):
        assert (
            Calculator.addition("2", 3)
            == "Invalid operation! alteast a variable is str"
        )
        assert (
            Calculator.addition(2, "3")
            == "Invalid operation! alteast a variable is str"
        )

    def test_subtraction_with_string(self):
        assert (
            Calculator.subtraction("5", 2)
            == "Invalid operation! alteast a variable is str"
        )

    def test_multiplication_with_string(self):
        assert (
            Calculator.multiplication(4, "3")
            == "Invalid operation! alteast a variable is str"
        )

    def test_division_by_zero(self):
        assert (
            Calculator.division(10, 0)
            == "ZeroDivisionError! division not supported when num2 is 0"
        )

    def test_floor_division_by_zero(self):
        assert (
            Calculator.floor_division(10, 0)
            == "ZeroDivisionError! floor_division not supported when num2 is 0"
        )

    def test_exponention_with_string(self):
        assert (
            Calculator.exponention(2, "3")
            == "Invalid operation! alteast a variable is str"
        )

    def test_addition_with_none(self):
        assert "Invalid operation!" in Calculator.addition(None, 3)

    def test_subtraction_with_none(self):
        assert "Invalid operation!" in Calculator.subtraction(5, None)

    def test_multiplication_with_float(self):
        assert Calculator.multiplication(2.5, 4) == 10.0

    def test_division_float_result(self):
        assert Calculator.division(7, 2) == 3.5

    def test_floor_division_negative(self):
        assert Calculator.floor_division(-7, 2) == -4

    def test_exponention_negative(self):
        assert Calculator.exponention(2, -2) == 0.25
