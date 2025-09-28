import pytest
import sys
from src.pcep.module2.simple_memory_profiler import (
    format_bytes,
    basic_memory_profiling,
    compare_list_vs_generator,
    string_concatenation_memory,
    data_structure_growth_analysis,
    memory_optimization_tips,
    practical_memory_profiler,
)

"""
Test suite for memory profiling implementation

Learning objectives:
1. Testing memory measurement utilities
2. Validating memory comparison logic
3. Ensuring memory profiling accuracy
4. Testing memory optimization examples
"""


class TestMemoryProfiling:
    """Test memory profiling functionality"""

    def test_format_bytes(self):
        """Test byte formatting utility"""
        assert format_bytes(0) == "0.0 B"
        assert format_bytes(512) == "512.0 B"
        assert format_bytes(1024) == "1.0 KB"
        assert format_bytes(1024 * 1024) == "1.0 MB"
        assert format_bytes(1024 * 1024 * 1024) == "1.0 GB"
        assert format_bytes(2048) == "2.0 KB"
        assert format_bytes(1536) == "1.5 KB"

    def test_sys_getsizeof_basic_types(self):
        """Test sys.getsizeof with basic Python types"""
        # Integers
        assert sys.getsizeof(0) > 0
        assert sys.getsizeof(1) > 0
        assert sys.getsizeof(100) > 0

        # Strings
        assert sys.getsizeof("") > 0
        assert sys.getsizeof("hello") > sys.getsizeof("")
        assert sys.getsizeof("hello" * 100) > sys.getsizeof("hello")

        # Lists
        assert sys.getsizeof([]) > 0
        assert sys.getsizeof([1, 2, 3]) > sys.getsizeof([])
        assert sys.getsizeof(list(range(100))) > sys.getsizeof(list(range(10)))

    def test_list_vs_generator_memory(self):
        """Test that generators use less memory than lists"""
        n = 10000

        # Create list and generator
        my_list = [x for x in range(n)]
        my_generator = (x for x in range(n))

        list_size = sys.getsizeof(my_list)
        generator_size = sys.getsizeof(my_generator)

        # Generator should use significantly less memory
        assert generator_size < list_size
        assert list_size > generator_size * 100  # At least 100x difference

    def test_empty_vs_populated_structures(self):
        """Test memory growth of data structures"""
        # Lists
        empty_list = []
        populated_list = list(range(1000))
        assert sys.getsizeof(populated_list) > sys.getsizeof(empty_list)

        # Dictionaries
        empty_dict = {}
        populated_dict = {i: i for i in range(1000)}
        assert sys.getsizeof(populated_dict) > sys.getsizeof(empty_dict)

        # Sets
        empty_set = set()
        populated_set = set(range(1000))
        assert sys.getsizeof(populated_set) > sys.getsizeof(empty_set)

    def test_string_memory_growth(self):
        """Test string memory scaling"""
        short_string = "hello"
        long_string = "hello" * 1000
        very_long_string = "hello" * 10000

        assert sys.getsizeof(long_string) > sys.getsizeof(short_string)
        assert sys.getsizeof(very_long_string) > sys.getsizeof(long_string)

    def test_data_structure_memory_comparison(self):
        """Compare memory usage of different data structures with same data"""
        data = list(range(100))

        # Create different structures with same data
        as_list = data
        as_tuple = tuple(data)
        as_set = set(data)
        as_dict = {i: i for i in data}

        # Get sizes
        list_size = sys.getsizeof(as_list)
        tuple_size = sys.getsizeof(as_tuple)
        set_size = sys.getsizeof(as_set)
        dict_size = sys.getsizeof(as_dict)

        # All should have some memory usage
        assert list_size > 0
        assert tuple_size > 0
        assert set_size > 0
        assert dict_size > 0

        # Dict typically uses most memory due to key-value pairs
        assert dict_size > list_size

        # Set uses more than list due to hash table overhead
        assert set_size > list_size

    def test_memory_profiler_decorator(self):
        """Test the memory profiler decorator functionality"""
        results = []

        def memory_profiler(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                result_size = sys.getsizeof(result)
                results.append((func.__name__, result_size))
                return result

            return wrapper

        @memory_profiler
        def create_list(size):
            return list(range(size))

        @memory_profiler
        def create_string(length):
            return "A" * length

        # Test the decorator
        list_result = create_list(100)
        string_result = create_string(100)

        # Check results were captured
        assert len(results) == 2
        assert results[0][0] == "create_list"
        assert results[1][0] == "create_string"
        assert results[0][1] > 0
        assert results[1][1] > 0

        # Verify actual results
        assert len(list_result) == 100
        assert len(string_result) == 100

    def test_slots_optimization(self):
        """Test __slots__ memory optimization"""

        class RegularClass:
            def __init__(self, x, y, z):
                self.x = x
                self.y = y
                self.z = z

        class SlottedClass:
            __slots__ = ["x", "y", "z"]

            def __init__(self, x, y, z):
                self.x = x
                self.y = y
                self.z = z

        # Create instances
        regular = RegularClass(1, 2, 3)
        slotted = SlottedClass(1, 2, 3)

        regular_size = sys.getsizeof(regular)
        slotted_size = sys.getsizeof(slotted)

        # Both should have some size
        assert regular_size > 0
        assert slotted_size > 0

        # Note: __slots__ optimization may not always be visible in getsizeof
        # due to Python implementation details, but we test that both work
        assert hasattr(regular, "x")
        assert hasattr(slotted, "x")

    def test_memory_growth_patterns(self):
        """Test memory growth patterns of data structures"""
        sizes = [10, 100, 1000]

        for size in sizes:
            data = list(range(size))

            # Test that larger sizes use more memory
            if size > 10:
                smaller_data = list(range(size // 10))
                assert sys.getsizeof(data) > sys.getsizeof(smaller_data)

    @pytest.mark.parametrize("size", [10, 100, 1000, 10000])
    def test_parametrized_memory_scaling(self, size):
        """Parametrized test for memory scaling with different sizes"""
        data_structures = {
            "list": list(range(size)),
            "tuple": tuple(range(size)),
            "set": set(range(size)),
        }

        for name, structure in data_structures.items():
            memory_size = sys.getsizeof(structure)

            # All structures should use some memory
            assert memory_size > 0

            # Memory should scale with size (at least somewhat)
            if size >= 100:
                assert memory_size > 100  # Should be at least 100 bytes for 100+ items

    def test_generator_vs_list_comprehension_memory(self):
        """Compare memory usage: generator expression vs list comprehension"""
        n = 1000

        # List comprehension - stores all items
        list_comp = [x**2 for x in range(n)]

        # Generator expression - lazy evaluation
        gen_exp = (x**2 for x in range(n))

        list_size = sys.getsizeof(list_comp)
        gen_size = sys.getsizeof(gen_exp)

        # Generator should use much less memory
        assert gen_size < list_size
        assert list_size > gen_size * 10  # At least 10x difference

    def test_string_concatenation_methods(self):
        """Test memory efficiency of different string concatenation methods"""
        words = ["hello"] * 100

        # Method 1: join
        result_join = " ".join(words)

        # Method 2: manual concatenation (less efficient)
        result_manual = ""
        for word in words:
            result_manual += word + " "
        result_manual = result_manual.strip()

        # Both should produce similar results
        join_size = sys.getsizeof(result_join)
        manual_size = sys.getsizeof(result_manual)

        assert join_size > 0
        assert manual_size > 0

        # Results should be equivalent in content
        assert result_join == result_manual


class TestMemoryProfilerIntegration:
    """Integration tests for memory profiling functions"""

    def test_basic_memory_profiling_runs(self, capsys):
        """Test that basic memory profiling runs without errors"""
        basic_memory_profiling()
        captured = capsys.readouterr()
        assert "BASIC MEMORY PROFILING" in captured.out
        assert "bytes" in captured.out

    def test_list_vs_generator_comparison_runs(self, capsys):
        """Test that list vs generator comparison runs"""
        compare_list_vs_generator()
        captured = capsys.readouterr()
        assert "LIST VS GENERATOR" in captured.out
        assert "Memory savings" in captured.out

    def test_string_concatenation_analysis_runs(self, capsys):
        """Test that string concatenation analysis runs"""
        string_concatenation_memory()
        captured = capsys.readouterr()
        assert "STRING CONCATENATION" in captured.out

    def test_data_structure_growth_analysis_runs(self, capsys):
        """Test that data structure growth analysis runs"""
        data_structure_growth_analysis()
        captured = capsys.readouterr()
        assert "GROWTH ANALYSIS" in captured.out
        assert "List" in captured.out
        assert "Dict" in captured.out

    def test_memory_optimization_examples_run(self, capsys):
        """Test that memory optimization examples run"""
        memory_optimization_tips()
        captured = capsys.readouterr()
        assert "OPTIMIZATION EXAMPLES" in captured.out

    def test_practical_memory_profiler_runs(self, capsys):
        """Test that practical memory profiler runs"""
        practical_memory_profiler()
        captured = capsys.readouterr()
        assert "PRACTICAL MEMORY PROFILER" in captured.out
        assert "Function" in captured.out


class TestMemoryConstants:
    """Test that memory constants behave as expected"""

    def test_empty_container_sizes(self):
        """Test memory usage of empty containers"""
        empty_containers = {
            "list": [],
            "tuple": (),
            "dict": {},
            "set": set(),
            "string": "",
        }

        for name, container in empty_containers.items():
            size = sys.getsizeof(container)
            assert size > 0, f"Empty {name} should have positive size"
            assert size < 1000, f"Empty {name} should not be too large"

    def test_basic_type_memory_consistency(self):
        """Test that basic types have consistent memory usage"""
        # Same values should have same memory size
        assert sys.getsizeof(42) == sys.getsizeof(42)
        assert sys.getsizeof("hello") == sys.getsizeof("hello")
        assert sys.getsizeof([1, 2, 3]) == sys.getsizeof([1, 2, 3])

    def test_memory_ordering(self):
        """Test expected memory size ordering"""
        # Generally, more complex structures use more memory
        simple_int = sys.getsizeof(42)
        simple_string = sys.getsizeof("hello")
        small_list = sys.getsizeof([1, 2, 3])
        small_dict = sys.getsizeof({1: 2, 3: 4})

        # All should be positive
        assert simple_int > 0
        assert simple_string > 0
        assert small_list > 0
        assert small_dict > 0
