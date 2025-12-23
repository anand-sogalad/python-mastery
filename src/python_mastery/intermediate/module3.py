from typing import Callable

# Defining and calling functions
# In python functions are defined using def keyword


def my_func():
    pass


# lambda functions
# lambda functions are anonymos functions defined using lambda

# syntax:
# lambda argument: expression
if __name__ == "__main__":
    square: Callable[[int], int] = lambda x: x**2
    print(square(10))


# recursion
# recursion is a function that calls itself
# it must have break point
def func(n: int):
    if n <= 1:
        return n
    return func(n - 1) + func(n - 2)


if __name__ == "__main__":
    print(func(5))


# closures
# closure is a nested function that remembers the data from the parent function (outer scope)
def closure_func(data: int):
    x = data

    def my_fun():
        return x

    return my_fun


if __name__ == "__main__":
    x = closure_func(10)
    print(x())


# Generators and Iterators
# Generators are functions that yield one value at a time
# Where as Iterators are class that does the same job of generators returning one value at a time
# it must implement next and iter methods
def generator(number: int):
    while number >= 0:
        yield number
        number -= 1


class Iterator:
    def __init__(self, start: int, stop: int, step: int = 1):
        self.__start = start
        self.__stop = stop
        self.__step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.__step > 0:
            if self.__start <= self.__stop:
                current = self.__start
                self.__start += self.__step
                return current
            else:
                raise StopIteration
        else:
            if self.__start >= self.__stop:
                current = self.__start
                self.__start += self.__step  # Works for negative step too
                return current
            else:
                raise StopIteration


if __name__ == "__main__":
    x = generator(10)
    y = Iterator(0, 10)
    for i in range(11):
        print(next(x))
        print(next(y))

    for i in Iterator(1, 10):
        print(i)

    for i in generator(10):
        print(i)
