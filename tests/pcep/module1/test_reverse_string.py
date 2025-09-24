import pytest
from src.pcep.module1.reverse_string import Solution


class TestReverseString:
    @pytest.fixture
    def solution(self):
        return Solution()

    def test_reverse_string_basic(self, solution):
        s = ["h", "e", "l", "l", "o"]
        expected = ["o", "l", "l", "e", "h"]
        result = solution.reverse_string(s)
        assert result == expected
        assert s == expected  # in-place modification

    def test_reverse_string_even_length(self, solution):
        s = ["H", "a", "n", "n", "a", "h"]
        expected = ["h", "a", "n", "n", "a", "H"]
        result = solution.reverse_string(s)
        assert result == expected
        assert s == expected

    def test_reverse_string_single_char(self, solution):
        s = ["a"]
        expected = ["a"]
        result = solution.reverse_string(s)
        assert result == expected
        assert s == expected

    def test_reverse_string_two_chars(self, solution):
        s = ["a", "b"]
        expected = ["b", "a"]
        result = solution.reverse_string(s)
        assert result == expected
        assert s == expected

    def test_reverse_string_long(self, solution):
        s = list("abcdefghijklmnopqrstuvwxyz")
        expected = list("zyxwvutsrqponmlkjihgfedcba")
        result = solution.reverse_string(s)
        assert result == expected
        assert s == expected

    def test_reverse_string_invalid_length_too_short(self, solution):
        s = []
        result = solution.reverse_string(s)
        assert result is None

    def test_reverse_string_invalid_length_too_long(self, solution):
        s = ["a"] * 106  # length 106 > 105
        result = solution.reverse_string(s)
        assert result is None

    def test_reverse_string_special_characters(self, solution):
        s = ["!", "@", "#", "$", "%"]
        expected = ["%", "$", "#", "@", "!"]
        result = solution.reverse_string(s)
        assert result == expected
        assert s == expected

    def test_reverse_string_numbers(self, solution):
        s = ["1", "2", "3", "4", "5"]
        expected = ["5", "4", "3", "2", "1"]
        result = solution.reverse_string(s)
        assert result == expected
        assert s == expected
