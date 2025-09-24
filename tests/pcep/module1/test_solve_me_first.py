import pytest
import sys
import os

# Add the src directory to Python path for imports
src_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "src")
)
sys.path.insert(0, src_path)

from src.pcep.module1.solve_me_first import solve_me_first, int_type_checker

"""
Test suite for solve_me_first function and int_type_checker decorator.

Learning objectives:
1. Testing decorated functions
2. Testing decorator behavior with valid/invalid inputs
3. Testing both positional and keyword arguments
4. Using pytest fixtures and parametrization
"""


class TestSolveMeFirst:
    """Test class for the solve_me_first function"""

    def test_solve_me_first_basic_addition(self):
        """Test basic integer addition"""
        assert solve_me_first(2, 3) == 5

    def test_solve_me_first_zero_values(self):
        """Test addition with zero values"""
        assert solve_me_first(0, 0) == 0
        assert solve_me_first(5, 0) == 5
        assert solve_me_first(0, 7) == 7

    def test_solve_me_first_negative_numbers(self):
        """Test addition with negative numbers"""
        assert solve_me_first(-2, 3) == 1
        assert solve_me_first(2, -3) == -1
        assert solve_me_first(-5, -3) == -8

    def test_solve_me_first_large_numbers(self):
        """Test addition with large numbers"""
        assert solve_me_first(1000000, 2000000) == 3000000
        assert solve_me_first(-1000000, 500000) == -500000

    def test_solve_me_first_keyword_arguments(self):
        """Test function works with keyword arguments"""
        assert solve_me_first(a=10, b=15) == 25
        assert solve_me_first(b=5, a=3) == 8  # Order shouldn't matter

    def test_solve_me_first_mixed_arguments(self):
        """Test function works with mixed positional and keyword arguments"""
        assert solve_me_first(5, b=10) == 15

    @pytest.mark.parametrize(
        "a,b,expected",
        [(1, 1, 2), (10, 20, 30), (-5, 5, 0), (100, -50, 50), (0, 999, 999)],
    )
    def test_solve_me_first_parametrized(self, a, b, expected):
        """Parametrized test for multiple input combinations"""
        assert solve_me_first(a, b) == expected


class TestIntTypeChecker:
    """Test class for the int_type_checker decorator behavior"""

    def test_decorator_allows_valid_integers(self):
        """Test that decorator allows valid integer inputs"""
        # This should work without raising an exception
        result = solve_me_first(5, 7)
        assert result == 12

    def test_decorator_rejects_float_positional_args(self):
        """Test that decorator rejects float positional arguments"""
        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first(2.5, 3)

        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first(2, 3.7)

        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first(1.1, 2.2)

    def test_decorator_rejects_string_positional_args(self):
        """Test that decorator rejects string positional arguments"""
        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first("2", 3)

        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first(2, "3")

    def test_decorator_rejects_none_positional_args(self):
        """Test that decorator rejects None positional arguments"""
        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first(None, 3)

        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first(2, None)

    def test_decorator_rejects_float_keyword_args(self):
        """Test that decorator rejects float keyword arguments"""
        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first(a=2.5, b=3)

        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first(a=2, b=3.7)

    def test_decorator_rejects_string_keyword_args(self):
        """Test that decorator rejects string keyword arguments"""
        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first(a="2", b=3)

        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first(a=2, b="3")

    def test_decorator_rejects_mixed_valid_invalid_args(self):
        """Test that decorator rejects when some args are valid, some invalid"""
        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first(5, b=3.5)  # Valid positional, invalid keyword

        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first(2.5, b=3)  # Invalid positional, valid keyword

    @pytest.mark.parametrize(
        "invalid_input",
        [
            (1.5, 2),
            (1, 2.5),
            ("1", 2),
            (1, "2"),
            (None, 2),
            (1, None),
            ([1], 2),
            (1, [2]),
            (
                True,
                2,
            ),  # Note: bool is subclass of int in Python, so this might actually pass!
            (
                1,
                False,
            ),  # Note: bool is subclass of int in Python, so this might actually pass!
        ],
    )
    def test_decorator_rejects_various_invalid_types(self, invalid_input):
        """Parametrized test for various invalid input types"""
        a, b = invalid_input
        # Skip bool tests since bool is a subclass of int in Python
        if isinstance(a, bool) or isinstance(b, bool):
            pytest.skip("Skipping bool test - bool is subclass of int in Python")

        with pytest.raises(
            TypeError, match="solve_me_first takes only int parameters!"
        ):
            solve_me_first(a, b)


class TestDecoratorOnOtherFunctions:
    """Test that the int_type_checker decorator works on other functions too"""

    def test_decorator_on_multiplication_function(self):
        """Test decorator works on a different function"""

        @int_type_checker
        def multiply(x, y):
            return x * y

        # Valid inputs
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10

        # Invalid inputs
        with pytest.raises(TypeError, match="multiply takes only int parameters!"):
            multiply(3.5, 4)

    def test_decorator_on_function_with_more_parameters(self):
        """Test decorator works on function with more than 2 parameters"""

        @int_type_checker
        def sum_three(x, y, z):
            return x + y + z

        # Valid inputs
        assert sum_three(1, 2, 3) == 6
        assert sum_three(x=1, y=2, z=3) == 6

        # Invalid inputs
        with pytest.raises(TypeError, match="sum_three takes only int parameters!"):
            sum_three(1, 2, 3.5)

    def test_decorator_preserves_function_metadata(self):
        """Test that decorator preserves original function metadata"""
        # Check that function name is preserved
        assert solve_me_first.__name__ == "solve_me_first"

        # Check that docstring is preserved (if any)
        # Since solve_me_first doesn't have a docstring, we'll test with a new function
        @int_type_checker
        def test_function(a, b):
            """Test function docstring"""
            return a + b

        assert test_function.__name__ == "test_function"
        assert test_function.__doc__ == "Test function docstring"


class TestEdgeCases:
    """Test edge cases and special scenarios"""

    def test_boolean_inputs_are_accepted(self):
        """Test that boolean inputs are accepted (since bool is subclass of int)"""
        # In Python, bool is a subclass of int (True=1, False=0)
        assert solve_me_first(True, False) == 1  # True + False = 1 + 0 = 1
        assert solve_me_first(True, True) == 2  # True + True = 1 + 1 = 2
        assert solve_me_first(False, False) == 0  # False + False = 0 + 0 = 0

    def test_very_large_integers(self):
        """Test with very large integers"""
        large_num1 = 10**18
        large_num2 = 10**17
        expected = large_num1 + large_num2
        assert solve_me_first(large_num1, large_num2) == expected

    def test_function_with_no_arguments_decorated(self):
        """Test decorator behavior when function has no arguments"""

        @int_type_checker
        def get_constant():
            return 42

        # Should work fine since no arguments to validate
        assert get_constant() == 42
