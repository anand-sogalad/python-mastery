import pytest
import time
from src.pcep.module1.two_sum import TowoSum, TwoSum1

"""
Test suite for Two Sum implementations comparing:
1. TowoSum - Brute Force O(n²) approach
2. TwoSum1 - Hash Map O(n) approach

Learning objectives:
1. Testing multiple implementations of the same problem
2. Comparing algorithm performance 
3. Ensuring both approaches give correct results
4. Edge case validation
"""


class TestTwoSumImplementations:
    """Test both Two Sum implementations with the same test cases"""

    def setup_method(self):
        """Setup test instances"""
        self.brute_force = TowoSum()
        self.hash_map = TwoSum1()

    def test_example1_both_implementations(self):
        """Test example 1: [2,7,11,15], target=9 → [0,1]"""
        nums = [2, 7, 11, 15]
        target = 9

        result_brute = self.brute_force.two_sum(nums, target)
        result_hash = self.hash_map.two_sum(nums, target)

        assert result_brute == [0, 1]
        assert result_hash == (0, 1)  # Note: hash returns tuple

        # Verify both solutions are mathematically correct
        assert nums[result_brute[0]] + nums[result_brute[1]] == target
        assert nums[result_hash[0]] + nums[result_hash[1]] == target

    def test_example2_both_implementations(self):
        """Test example 2: [3,2,4], target=6 → [1,2]"""
        nums = [3, 2, 4]
        target = 6

        result_brute = self.brute_force.two_sum(nums, target)
        result_hash = self.hash_map.two_sum(nums, target)

        assert result_brute == [1, 2]
        assert result_hash == (1, 2)

        # Verify correctness
        assert nums[result_brute[0]] + nums[result_brute[1]] == target
        assert nums[result_hash[0]] + nums[result_hash[1]] == target

    def test_example3_both_implementations(self):
        """Test example 3: [3,3], target=6 → [0,1]"""
        nums = [3, 3]
        target = 6

        result_brute = self.brute_force.two_sum(nums, target)
        result_hash = self.hash_map.two_sum(nums, target)

        assert result_brute == [0, 1]
        assert result_hash == (0, 1)

        # Verify correctness
        assert nums[result_brute[0]] + nums[result_brute[1]] == target
        assert nums[result_hash[0]] + nums[result_hash[1]] == target

    def test_negative_numbers_both(self):
        """Test with negative numbers"""
        nums = [-1, -2, -3, -4, -5]
        target = -8

        result_brute = self.brute_force.two_sum(nums, target)
        result_hash = self.hash_map.two_sum(nums, target)

        # Both should find valid indices
        assert len(result_brute) == 2
        assert len(result_hash) == 2

        # Verify correctness
        assert nums[result_brute[0]] + nums[result_brute[1]] == target
        assert nums[result_hash[0]] + nums[result_hash[1]] == target

    def test_mixed_positive_negative_both(self):
        """Test with mix of positive and negative numbers"""
        nums = [-3, 4, 3, 90]
        target = 0

        result_brute = self.brute_force.two_sum(nums, target)
        result_hash = self.hash_map.two_sum(nums, target)

        # Verify correctness
        assert nums[result_brute[0]] + nums[result_brute[1]] == target
        assert nums[result_hash[0]] + nums[result_hash[1]] == target

    def test_large_numbers_both(self):
        """Test with large numbers within constraints"""
        nums = [1000000000, -500000000]
        target = 500000000

        result_brute = self.brute_force.two_sum(nums, target)
        result_hash = self.hash_map.two_sum(nums, target)

        assert result_brute == [0, 1]
        assert result_hash == (0, 1)

    def test_minimum_array_size_both(self):
        """Test with minimum array size (2 elements)"""
        nums = [1, 2]
        target = 3

        result_brute = self.brute_force.two_sum(nums, target)
        result_hash = self.hash_map.two_sum(nums, target)

        assert result_brute == [0, 1]
        assert result_hash == (0, 1)

    @pytest.mark.parametrize(
        "nums,target",
        [
            ([2, 7, 11, 15], 9),
            ([3, 2, 4], 6),
            ([3, 3], 6),
            ([0, 4, 3, 0], 0),
            ([-1, 0], -1),
            ([1, 5, 2, 3], 4),
            ([-5, -2, 1, 8], 6),
        ],
    )
    def test_parametrized_both_implementations(self, nums, target):
        """Parametrized test ensuring both implementations give valid results"""
        result_brute = self.brute_force.two_sum(nums.copy(), target)
        result_hash = self.hash_map.two_sum(nums.copy(), target)

        # Both should return valid indices
        assert len(result_brute) == 2
        assert len(result_hash) == 2

        # Both solutions should be mathematically correct
        assert nums[result_brute[0]] + nums[result_brute[1]] == target
        assert nums[result_hash[0]] + nums[result_hash[1]] == target

        # Indices should be different (no same element twice)
        assert result_brute[0] != result_brute[1]
        assert result_hash[0] != result_hash[1]


class TestBruteForceSpecific:
    """Tests specific to the brute force implementation"""

    def setup_method(self):
        self.solution = TowoSum()

    def test_returns_list(self):
        """Test that brute force returns a list"""
        result = self.solution.two_sum([1, 2], 3)
        assert isinstance(result, list)
        assert result == [0, 1]

    def test_finds_first_valid_pair(self):
        """Test that it finds the first valid pair in order"""
        nums = [1, 2, 3, 4, 2]  # Multiple solutions possible
        target = 4
        result = self.solution.two_sum(nums, target)
        # Should find [1, 3] (indices 0, 2) → 1 + 3 = 4
        assert result == [0, 2]  # 1 + 3 = 4


class TestHashMapSpecific:
    """Tests specific to the hash map implementation"""

    def setup_method(self):
        self.solution = TwoSum1()

    def test_returns_tuple(self):
        """Test that hash map solution returns a tuple"""
        result = self.solution.two_sum([1, 2], 3)
        assert isinstance(result, tuple)
        assert result == (0, 1)

    def test_handles_duplicates_correctly(self):
        """Test that hash map correctly handles duplicate values"""
        nums = [3, 3]
        target = 6
        result = self.solution.two_sum(nums, target)
        assert result == (0, 1)  # Should find both indices

    def test_overwrites_hash_correctly(self):
        """Test hash map overwrites previous indices correctly"""
        nums = [2, 5, 2, 11]  # Two 2's at indices 0 and 2
        target = 4  # 2 + 2 = 4
        result = self.solution.two_sum(nums, target)
        # Should return (0, 2) since hash map stores the latest index
        assert result == (0, 2)


class TestPerformanceComparison:
    """Compare performance between both implementations"""

    def test_performance_on_large_input(self):
        """Compare performance on larger datasets"""
        # Create a large test case where solution is at the end
        size = 1000
        nums = list(range(size))
        nums.append(0)  # Now we have [0,1,2,...,999,0]
        target = size - 1  # 999, so we need indices 999 and 1000

        brute_force = TowoSum()
        hash_map = TwoSum1()

        # Time brute force
        start_time = time.time()
        result_brute = brute_force.two_sum(nums.copy(), target)
        brute_time = time.time() - start_time

        # Time hash map
        start_time = time.time()
        result_hash = hash_map.two_sum(nums.copy(), target)
        hash_time = time.time() - start_time

        # Both should find valid solutions
        assert nums[result_brute[0]] + nums[result_brute[1]] == target
        assert nums[result_hash[0]] + nums[result_hash[1]] == target

        # Print timing for educational purposes
        print(f"\\nPerformance Comparison (n={size+1}):")
        print(f"Brute Force O(n²): {brute_time:.6f} seconds")
        print(f"Hash Map O(n):     {hash_time:.6f} seconds")
        if hash_time > 0:
            print(f"Speedup: {brute_time/hash_time:.2f}x")

        # Hash map should generally be faster for large inputs
        # (Though for small inputs, brute force might be faster due to overhead)


class TestEdgeCases:
    """Test edge cases for both implementations"""

    def setup_method(self):
        self.brute_force = TowoSum()
        self.hash_map = TwoSum1()

    def test_zero_target(self):
        """Test when target is zero"""
        nums = [-1, 0, 1, 2, -1, -4]
        target = 0

        result_brute = self.brute_force.two_sum(nums, target)
        result_hash = self.hash_map.two_sum(nums, target)

        # Verify correctness
        assert nums[result_brute[0]] + nums[result_brute[1]] == target
        assert nums[result_hash[0]] + nums[result_hash[1]] == target

    def test_negative_target(self):
        """Test with negative target"""
        nums = [-1, -2, -3, -4]
        target = -5

        result_brute = self.brute_force.two_sum(nums, target)
        result_hash = self.hash_map.two_sum(nums, target)

        # Verify correctness
        assert nums[result_brute[0]] + nums[result_brute[1]] == target
        assert nums[result_hash[0]] + nums[result_hash[1]] == target

    def test_maximum_constraints(self):
        """Test with values at constraint boundaries"""
        nums = [1000000000, -1000000000]
        target = 0

        result_brute = self.brute_force.two_sum(nums, target)
        result_hash = self.hash_map.two_sum(nums, target)

        assert result_brute == [0, 1]
        assert result_hash == (0, 1)
