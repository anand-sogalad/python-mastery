# Practice: CLI apps for string/number manipulations, operator overloading


class Person:
    def __init__(self, name, age, weight):
        self.__name = name
        self.__age = age
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if not (1 <= weight <= 100):
            raise ValueError("Person weight can be only within 1, 100")
        self.__weight = weight

    def __add__(self, other):
        return self.weight + other.weight


class Addition:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other.value, (int, float)) and isinstance(
            self.value, (int, float)
        ):
            return self.value + other.value
        if isinstance(other.value, str) and isinstance(self.value, str):
            return self.value + " " + other.value
        raise TypeError(
            f"Cannot do additoin between {type(self.value)} and {type(other.value)}"
        )
