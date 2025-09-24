"""
Complete the function  to compute the sum of two integers.

Example


Return .

Function Description

Complete the  function with the following parameters:

: the first value
: the second value
Returns
- : the sum of  and

Constraints


Sample Input

a = 2
b = 3
Sample Output

5
Explanation

.
"""

import functools


def int_type_checker(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Check positional arguments
        if not all(isinstance(arg, int) for arg in args):
            raise TypeError(f"{func.__name__} takes only int parameters!")

        # Check keyword arguments
        if not all(isinstance(value, int) for value in kwargs.values()):
            raise TypeError(f"{func.__name__} takes only int parameters!")

        return func(*args, **kwargs)

    return wrapper


@int_type_checker
def solve_me_first(a, b):
    return a + b
