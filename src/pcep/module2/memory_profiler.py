"""
Memory Profiling with sys.getsizeof - Comprehensive Implementation

Learning objectives:
1. Understanding memory footprint of different data structures
2. Comparing memory efficiency between approaches
3. Memory profiling for optimization decisions
4. Deep vs shallow memory analysis
"""

import sys
import gc
from typing import Any, Dict, List
from functools import wraps
import time


class MemoryProfiler:
    """Advanced memory profiling utility using sys.getsizeof"""

    def __init__(self):
        self.measurements = {}

    @staticmethod
    def get_size(obj: Any, seen: set = None) -> int:
        """
        Get deep memory size of an object including all referenced objects

        Args:
            obj: Object to measure
            seen: Set to track already counted objects (prevents infinite recursion)

        Returns:
            Total memory size in bytes
        """
        if seen is None:
            seen = set()

        obj_id = id(obj)
        if obj_id in seen:
            return 0

        seen.add(obj_id)
        size = sys.getsizeof(obj)

        # Handle different types
        if isinstance(obj, dict):
            size += sum(
                MemoryProfiler.get_size(v, seen) + MemoryProfiler.get_size(k, seen)
                for k, v in obj.items()
            )
        elif hasattr(obj, "__dict__"):
            size += MemoryProfiler.get_size(obj.__dict__, seen)
        elif hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes, bytearray)):
            size += sum(MemoryProfiler.get_size(i, seen) for i in obj)

        return size

    @staticmethod
    def format_bytes(bytes_size: int) -> str:
        """Convert bytes to human readable format"""
        for unit in ["B", "KB", "MB", "GB"]:
            if bytes_size < 1024:
                return f"{bytes_size:.2f} {unit}"
            bytes_size /= 1024
        return f"{bytes_size:.2f} TB"

    def profile_memory(self, label: str = "measurement"):
        """Decorator to profile memory usage of a function"""

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # Measure before
                gc.collect()  # Force garbage collection
                mem_before = self.get_current_memory()

                # Execute function
                start_time = time.time()
                result = func(*args, **kwargs)
                exec_time = time.time() - start_time

                # Measure after
                gc.collect()
                mem_after = self.get_current_memory()

                # Calculate result memory
                result_size = self.get_size(result) if result is not None else 0

                # Store measurements
                self.measurements[label] = {
                    "function": func.__name__,
                    "memory_before": mem_before,
                    "memory_after": mem_after,
                    "memory_delta": mem_after - mem_before,
                    "result_size": result_size,
                    "execution_time": exec_time,
                    "args_size": sum(self.get_size(arg) for arg in args),
                    "kwargs_size": self.get_size(kwargs),
                }

                return result

            return wrapper

        return decorator

    @staticmethod
    def get_current_memory() -> int:
        """Get current process memory usage (approximation)"""
        try:
            import psutil

            process = psutil.Process()
            return process.memory_info().rss
        except ImportError:
            # Fallback: sum of all objects in gc
            return sum(sys.getsizeof(obj) for obj in gc.get_objects())

    def print_report(self, label: str = None):
        """Print memory profiling report"""
        if label and label in self.measurements:
            measurements = {label: self.measurements[label]}
        else:
            measurements = self.measurements

        print("=" * 80)
        print("MEMORY PROFILING REPORT")
        print("=" * 80)

        for label, data in measurements.items():
            print(f"\nFunction: {data['function']} [{label}]")
            print(f"Execution Time: {data['execution_time']:.4f} seconds")
            print(f"Memory Before:  {self.format_bytes(data['memory_before'])}")
            print(f"Memory After:   {self.format_bytes(data['memory_after'])}")
            print(f"Memory Delta:   {self.format_bytes(data['memory_delta'])}")
            print(f"Result Size:    {self.format_bytes(data['result_size'])}")
            print(f"Args Size:      {self.format_bytes(data['args_size'])}")
            print(f"Kwargs Size:    {self.format_bytes(data['kwargs_size'])}")
            print("-" * 40)


def compare_data_structures():
    """Compare memory usage of different data structures"""
    print("=" * 60)
    print("DATA STRUCTURE MEMORY COMPARISON")
    print("=" * 60)

    # Test data
    n = 10000
    data = list(range(n))

    # Different data structures
    structures = {
        "list": list(data),
        "tuple": tuple(data),
        "set": set(data),
        "dict_keys": {i: i for i in data},
        "generator": (x for x in data),  # Note: generator size is misleading
    }

    print(f"Comparing structures with {n:,} elements:")
    print(
        f"{'Structure':<15} {'Shallow Size':<15} {'Deep Size':<15} {'Per Element':<15}"
    )
    print("-" * 65)

    for name, struct in structures.items():
        shallow_size = sys.getsizeof(struct)
        deep_size = MemoryProfiler.get_size(struct)
        per_element = deep_size / len(data) if hasattr(struct, "__len__") else 0

        print(
            f"{name:<15} {MemoryProfiler.format_bytes(shallow_size):<15} "
            f"{MemoryProfiler.format_bytes(deep_size):<15} "
            f"{MemoryProfiler.format_bytes(per_element):<15}"
        )


def compare_algorithms():
    """Compare memory usage of different algorithms"""
    profiler = MemoryProfiler()

    @profiler.profile_memory("list_comprehension")
    def list_comprehension_approach(n):
        return [x**2 for x in range(n)]

    @profiler.profile_memory("generator_expression")
    def generator_approach(n):
        return (x**2 for x in range(n))

    @profiler.profile_memory("traditional_loop")
    def traditional_loop_approach(n):
        result = []
        for x in range(n):
            result.append(x**2)
        return result

    @profiler.profile_memory("numpy_array")
    def numpy_approach(n):
        try:
            import numpy as np

            arr = np.arange(n)
            return arr**2
        except ImportError:
            return list(range(n))  # Fallback

    print("=" * 60)
    print("ALGORITHM MEMORY COMPARISON")
    print("=" * 60)

    n = 100000
    print(f"Comparing algorithms for processing {n:,} numbers:")

    # Run comparisons
    result1 = list_comprehension_approach(n)
    result2 = generator_approach(n)
    result3 = traditional_loop_approach(n)
    result4 = numpy_approach(n)

    profiler.print_report()


def memory_optimization_example():
    """Example of memory optimization using profiling"""
    profiler = MemoryProfiler()

    @profiler.profile_memory("memory_heavy")
    def memory_heavy_approach(data):
        # Creates multiple intermediate lists
        step1 = [x * 2 for x in data]
        step2 = [x + 1 for x in step1]
        step3 = [x**2 for x in step2]
        return step3

    @profiler.profile_memory("memory_optimized")
    def memory_optimized_approach(data):
        # Single comprehension, no intermediate storage
        return [(x * 2 + 1) ** 2 for x in data]

    @profiler.profile_memory("generator_optimized")
    def generator_optimized_approach(data):
        # Generator approach for lazy evaluation
        def process_item(x):
            return (x * 2 + 1) ** 2

        return (process_item(x) for x in data)

    print("=" * 60)
    print("MEMORY OPTIMIZATION EXAMPLE")
    print("=" * 60)

    test_data = list(range(50000))
    print(f"Processing {len(test_data):,} numbers...")

    # Run different approaches
    result1 = memory_heavy_approach(test_data)
    result2 = memory_optimized_approach(test_data)
    result3 = generator_optimized_approach(test_data)

    profiler.print_report()

    # Convert generator to list to see actual memory usage
    print("\nConverting generator to list:")
    gen_as_list = list(result3)
    gen_list_size = MemoryProfiler.get_size(gen_as_list)
    print(f"Generator as list size: {MemoryProfiler.format_bytes(gen_list_size)}")


def class_memory_profiling():
    """Profile memory usage of custom classes"""

    class SimpleClass:
        def __init__(self, data):
            self.data = data

    class OptimizedClass:
        __slots__ = ["data"]  # Reduces memory overhead

        def __init__(self, data):
            self.data = data

    class DataClass:
        def __init__(self, data):
            self.data = data
            self.metadata = {"created": time.time(), "size": len(data)}

    print("=" * 60)
    print("CLASS MEMORY PROFILING")
    print("=" * 60)

    test_data = list(range(1000))

    # Create instances
    simple_obj = SimpleClass(test_data)
    optimized_obj = OptimizedClass(test_data)
    data_obj = DataClass(test_data)

    # Compare sizes
    objects = {
        "SimpleClass": simple_obj,
        "OptimizedClass (__slots__)": optimized_obj,
        "DataClass (with metadata)": data_obj,
        "Raw data (list)": test_data,
    }

    print(f"{'Object Type':<25} {'Shallow Size':<15} {'Deep Size':<15}")
    print("-" * 55)

    for name, obj in objects.items():
        shallow = sys.getsizeof(obj)
        deep = MemoryProfiler.get_size(obj)
        print(
            f"{name:<25} {MemoryProfiler.format_bytes(shallow):<15} "
            f"{MemoryProfiler.format_bytes(deep):<15}"
        )


def main():
    """Run all memory profiling examples"""
    print("PYTHON MEMORY PROFILING WITH sys.getsizeof")
    print("=" * 80)

    # Run all examples
    compare_data_structures()
    print("\n")

    compare_algorithms()
    print("\n")

    memory_optimization_example()
    print("\n")

    class_memory_profiling()

    print("\n" + "=" * 80)
    print("MEMORY PROFILING TIPS:")
    print("• Use sys.getsizeof() for shallow size measurement")
    print("• Implement deep size calculation for nested structures")
    print("• Profile before and after optimizations")
    print("• Consider generators for large datasets")
    print("• Use __slots__ to reduce class overhead")
    print("• Force garbage collection for accurate measurements")
    print("=" * 80)


if __name__ == "__main__":
    main()
