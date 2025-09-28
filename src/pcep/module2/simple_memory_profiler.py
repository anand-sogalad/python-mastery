"""
Simple Memory Profiling Examples using sys.getsizeof

Learning objectives:
1. Basic memory measurement with sys.getsizeof
2. Comparing memory efficiency of different approaches
3. Understanding memory growth patterns
4. Practical memory optimization techniques
"""

import sys
from typing import List, Generator


def basic_memory_profiling():
    """Basic examples of memory profiling with sys.getsizeof"""
    print("=" * 50)
    print("BASIC MEMORY PROFILING")
    print("=" * 50)

    # Different data types
    data_samples = {
        "Empty list": [],
        "List with 10 items": list(range(10)),
        "List with 1000 items": list(range(1000)),
        "Empty string": "",
        "Short string": "Hello",
        "Long string": "Hello" * 1000,
        "Empty dict": {},
        "Dict with 10 items": {i: i * 2 for i in range(10)},
        "Empty set": set(),
        "Set with 10 items": set(range(10)),
    }

    print(f"{'Data Type':<25} {'Size (bytes)':<15} {'Human Readable':<15}")
    print("-" * 55)

    for name, data in data_samples.items():
        size = sys.getsizeof(data)
        human_size = format_bytes(size)
        print(f"{name:<25} {size:<15} {human_size:<15}")


def format_bytes(bytes_size: int) -> str:
    """Convert bytes to human-readable format"""
    for unit in ["B", "KB", "MB", "GB"]:
        if bytes_size < 1024:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.1f} TB"


def compare_list_vs_generator():
    """Compare memory usage: List vs Generator"""
    print("\n" + "=" * 50)
    print("LIST VS GENERATOR MEMORY COMPARISON")
    print("=" * 50)

    n = 100000

    # List approach - stores all items in memory
    def create_list(size: int) -> List[int]:
        return [x**2 for x in range(size)]

    # Generator approach - lazy evaluation
    def create_generator(size: int) -> Generator[int, None, None]:
        return (x**2 for x in range(size))

    # Measure memory
    my_list = create_list(n)
    my_generator = create_generator(n)

    list_size = sys.getsizeof(my_list)
    generator_size = sys.getsizeof(my_generator)

    print(f"Processing {n:,} numbers:")
    print(f"List memory:      {format_bytes(list_size):>10} ({list_size:,} bytes)")
    print(
        f"Generator memory: {format_bytes(generator_size):>10} ({generator_size:,} bytes)"
    )
    print(f"Memory savings:   {format_bytes(list_size - generator_size):>10}")
    print(f"Reduction factor: {list_size / generator_size:.1f}x smaller")


def string_concatenation_memory():
    """Compare memory efficiency of string operations"""
    print("\n" + "=" * 50)
    print("STRING CONCATENATION MEMORY ANALYSIS")
    print("=" * 50)

    # Different approaches to building strings
    def concat_with_plus(words: List[str]) -> str:
        result = ""
        for word in words:
            result += word + " "
        return result

    def concat_with_join(words: List[str]) -> str:
        return " ".join(words)

    def concat_with_list(words: List[str]) -> str:
        result = []
        for word in words:
            result.append(word)
        return " ".join(result)

    # Test data
    words = ["hello"] * 1000

    # Measure results
    result1 = concat_with_plus(words)
    result2 = concat_with_join(words)
    result3 = concat_with_list(words)

    print(f"Concatenating {len(words):,} words:")
    print(f"String += approach:   {format_bytes(sys.getsizeof(result1)):>10}")
    print(f"String join approach: {format_bytes(sys.getsizeof(result2)):>10}")
    print(f"List + join approach: {format_bytes(sys.getsizeof(result3)):>10}")

    # Show input size for reference
    print(f"Original word list:   {format_bytes(sys.getsizeof(words)):>10}")


def data_structure_growth_analysis():
    """Analyze how data structures grow with size"""
    print("\n" + "=" * 50)
    print("DATA STRUCTURE GROWTH ANALYSIS")
    print("=" * 50)

    sizes = [10, 100, 1000, 10000]

    print(f"{'Size':<10} {'List':<10} {'Tuple':<10} {'Set':<10} {'Dict':<10}")
    print("-" * 50)

    for size in sizes:
        data = list(range(size))

        list_size = sys.getsizeof(data)
        tuple_size = sys.getsizeof(tuple(data))
        set_size = sys.getsizeof(set(data))
        dict_size = sys.getsizeof({i: i for i in data})

        print(
            f"{size:<10} {format_bytes(list_size):<10} "
            f"{format_bytes(tuple_size):<10} {format_bytes(set_size):<10} "
            f"{format_bytes(dict_size):<10}"
        )


def memory_optimization_tips():
    """Demonstrate memory optimization techniques"""
    print("\n" + "=" * 50)
    print("MEMORY OPTIMIZATION EXAMPLES")
    print("=" * 50)

    # Example 1: Using slots to reduce class overhead
    class RegularClass:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class OptimizedClass:
        __slots__ = ["x", "y"]

        def __init__(self, x, y):
            self.x = x
            self.y = y

    # Create instances
    regular = RegularClass(10, 20)
    optimized = OptimizedClass(10, 20)

    print("Class Memory Optimization with __slots__:")
    print(f"Regular class:   {sys.getsizeof(regular)} bytes")
    print(f"Optimized class: {sys.getsizeof(optimized)} bytes")
    print(f"Memory savings:  {sys.getsizeof(regular) - sys.getsizeof(optimized)} bytes")

    # Example 2: List comprehension vs traditional loops
    n = 10000

    # Measure intermediate storage
    def traditional_filter(data):
        temp = []
        for x in data:
            if x % 2 == 0:
                temp.append(x * 2)
        return temp

    def optimized_filter(data):
        return [x * 2 for x in data if x % 2 == 0]

    test_data = list(range(n))
    result1 = traditional_filter(test_data)
    result2 = optimized_filter(test_data)

    print(f"\nList Processing (filtering {n:,} numbers):")
    print(f"Traditional result: {format_bytes(sys.getsizeof(result1))}")
    print(f"Optimized result:   {format_bytes(sys.getsizeof(result2))}")


def practical_memory_profiler():
    """Simple decorator for profiling function memory usage"""
    print("\n" + "=" * 50)
    print("PRACTICAL MEMORY PROFILER")
    print("=" * 50)

    def memory_profiler(func):
        """Simple decorator to measure function result memory usage"""

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result_size = sys.getsizeof(result)
            print(f"Function '{func.__name__}' result: {format_bytes(result_size)}")
            return result

        return wrapper

    # Example usage
    @memory_profiler
    def create_large_list(size):
        return list(range(size))

    @memory_profiler
    def create_large_dict(size):
        return {i: i * 2 for i in range(size)}

    @memory_profiler
    def create_string_data(length):
        return "A" * length

    # Test the profiler
    create_large_list(10000)
    create_large_dict(5000)
    create_string_data(50000)


def main():
    """Run all memory profiling examples"""
    print("MEMORY PROFILING WITH sys.getsizeof")
    print("=" * 60)

    basic_memory_profiling()
    compare_list_vs_generator()
    string_concatenation_memory()
    data_structure_growth_analysis()
    memory_optimization_tips()
    practical_memory_profiler()

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("• sys.getsizeof() measures shallow object size")
    print("• Generators use constant memory regardless of data size")
    print("• String join() is more memory efficient than += concatenation")
    print("• __slots__ can significantly reduce class instance overhead")
    print("• List comprehensions often more memory efficient than loops")
    print("• Always profile before and after optimizations")
    print("=" * 60)


if __name__ == "__main__":
    main()
