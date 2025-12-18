# Module and packages

# What is module in python?
# A module is nothing but a python file that has .py extension

# What is package?
# A package is a collection of modules
# and should have __init__.py file to make a directory or folder act as package

# Let's try to import modules and entities from different packages
from python_mastery.beginner.module1 import number
from python_mastery.beginner.module2 import INT
from python_mastery.intermediate.module1.inner.module1 import INT as integer

if __name__ == "__main__":
    print(number)
    print(INT)
    print(integer)


# standard library modules
import math


def sqrt(number: int):
    return math.sqrt(number)


def pi():
    return math.pi


def ceil(number: float | int):
    return math.ceil(number)
