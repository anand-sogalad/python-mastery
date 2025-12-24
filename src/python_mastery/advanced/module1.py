# OOP foundation

# What is class: A class is representation of a class. it's a blueprint
# Instance: It is a instance of a class
# Object: Its a representaion of data and methods
# attribute: these are the properties
# methods: these describe the behaviours

# Example of a class
from abc import ABC, abstractmethod
from functools import wraps
from typing import Literal


class Duck:
    species = "Duck"
    counter: int = 0

    def __init__(self, height: float, weight: float, sex: Literal["male", "female"]):
        self.height = height
        self.weight = weight
        self.sex = sex
        Duck.counter += 1

    def walk(self):
        print(f"{self.species} going for walk")


class Chicken:
    species = "Chicken"
    counter: int = 0

    def __init__(self, height: float, weight: float, sex: Literal["male", "female"]):
        self.height = height
        self.weight = weight
        self.sex = sex
        Chicken.counter += 1

    def walk(self):
        print(f"{self.species} going for walk")


if __name__ == "__main__":
    # creating instances of Duck class
    duckling = Duck(height=10, weight=3.4, sex="male")
    drake = Duck(height=25, weight=3.7, sex="male")
    hen = Chicken(height=20, weight=3.4, sex="female")

    for poultry in duckling, drake, hen:
        print(f"I am of type: {type(poultry)}")
        print(f"Species: {poultry.species} count: {poultry.counter}")
        poultry.walk()


# decorators
# Decorators are higher order functions, that modifies the behaviour of the function it wraps
def logger(prefix="LOG", level="INFO"):
    """Decorator factory that accepts arguments"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{prefix}:{level}] I am decorated")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@logger(prefix="DEBUG", level="TRACE")
def greet():
    print("I am greeting")


@logger()  # Using default arguments
def farewell():
    print("Goodbye!")


# Singleton class decorator
def singleton(cls):
    """Decorator that converts a class into a singleton"""
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Database:
    """Singleton database connection"""

    def __init__(self, host="localhost", port=5432):
        self.host = host
        self.port = port
        print(f"Database connection created: {host}:{port}")

    def query(self, sql):
        return f"Executing: {sql}"


# abstract class
# A class the acts as base class but cannot be instantiated and have atleast one abstract method
class Animal(ABC):
    @abstractmethod
    def eat(self): ...

    @abstractmethod
    def sleep(self): ...


class Person(Animal):
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("can eat veg or non veg based on the day, time and mood that is human!!!!")

    def sleep(self):
        print("Can sleep 24hr a day, but not a healthy habbit")


if __name__ == "__main__":
    greet()
    farewell()

    # Singleton example
    print("\n--- Singleton Pattern ---")
    db1 = Database(host="server1", port=3306)
    db2 = Database(host="server2", port=5432)  # These args are ignored
    db3 = Database()

    print(f"db1 is db2: {db1 is db2}")  # True - same instance
    print(f"db1 is db3: {db1 is db3}")  # True - same instance
    print(f"db1.host: {db1.host}, db2.host: {db2.host}")  # Both show server1

    vijay = Person("Vijay", 32, 170, 70)
    vijay.eat()
    vijay.sleep()
