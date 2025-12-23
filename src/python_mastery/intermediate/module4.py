# Classes and Objects
# What is class: A class is blueprint for creating an object
# What is an object: An object is a instance of an class

# creating class
from typing import override


class Class1:  # sample class1
    pass


class Class2:  # sample class2
    pass


# __init__ method
# this is a special method generally used for initilzing the instance and instance vartiables
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age


# instance variables vs class variables
# instance variables created and present only during the lifetime of the instance and operates on the instance itself
# class variables created during and present in enteir class lifetime, available in all the instance life time as well. and operate on class itself


class Example:
    instances = 0  # class variable

    def __init__(self, name: str):
        Example.instances += 1
        self.name = name  # instance variable


if __name__ == "__main__":
    obj1 = Example("abc")
    obj2 = Example("xyz")

    print(obj1.name)
    print(obj2.name)
    print(obj1.instances)
    print(obj2.instances)
    print(Example.instances)


# methods
# Instance methods: Instance method operates on instance variables and bound to instance
# Class methods: class method operates on class variables and bound to calss
# Static methods: static method is a utiltiy method doesnt bind dirsctly either to class or instance data/variables
# can directly called using class name


class Person1:
    __instance_count = 0  # class variable

    def __init__(self, name: str):  # constructor
        self.name = name
        Person1.__instance_count += 1

    @property
    def name(self):  # instance method acrts as property
        return self.__name

    @name.setter
    def name(self, name: str):  # instance method acts as property
        self.__name = name

    def is_rich(self):  # instance method
        return True

    @classmethod
    def get_instance_count(cls):
        return cls.__instance_count

    @staticmethod
    def walk():
        return "Person1 has walking ability"


if __name__ == "__main__":
    obj1 = Person1("ABC")
    obj2 = Person1("XYZ")

    print(obj1.name)
    print(obj2.name)
    print(obj1.get_instance_count())
    print(obj1.walk())

# Inheritance
# Inheriting is the process inheriting properties and behaviours from parent class to subclass and enhance the capability of subclass
# Python support single, multiple and multilevel inheritance


# parent class 1
class Parent1(object):
    def parent1_method(self):
        print("parent1 method is being called")


# parent class 2
class Parent2(object):
    def parent2_method(self):
        print("parent2 method is being called")


# single inheritance
class Sub1(Parent1):
    def sub1_method(self):
        print("sub1 method is being called")


# multiple inheritance
class Sub2(Parent1, Parent2):
    def sub2_method(self):
        print("sub2 method is being called")

    @override
    def parent1_method(self):
        print("parent1 is printing sub2 class")
        super().parent1_method()  # accessing parent method using super()


if __name__ == "__main__":
    sub1 = Sub1()
    sub1.parent1_method()  # as sub1 is inherited from Parent1, sub1 class can assess them
    sub1.sub1_method()  # this is directly from sub1 class itself

    sub2 = Sub2()  # this is mutiple inherited object
    sub2.parent1_method()  # this method got overridden now in sub class
    sub2.parent2_method()
    sub2.sub2_method()

# Encapsulation
# Encapsulation is the process of binding the data into methods and hiding data and preventing the direct access to data

# Polymarphism
# The meanig of polymorphism is that same name but different forms
# in python we can achieve polymorphism through method overriding and duck typing


# Duck typing is done using common interface in python
class Cat:
    def run(self):
        print("cat is running")


class Dog:
    def run(self):
        print("dog is running")


def run(obj: Cat | Dog):
    obj.run()


if __name__ == "__main__":
    run(Cat())
    run(Dog())


# special methods
class Str:
    def __init__(self, string: str):
        self.string = string

    # this is used to print the object information
    def __str__(self):
        return self.string

    # used as raw string representation of object
    def __repr__(self):
        return f"I am a string: {self.string}"

    # used to override len() function affect on the object
    def __len__(self):
        return len(self.string)

    # used for concatination
    def __add__(self, other: Str):
        return self.string + other.string

    def __eq__(self, other: Str):
        return self.string == other.string


if __name__ == "__main__":
    my_string = Str("string1")
    my_string1 = Str("string1")
    my_string2 = Str("string2")

    print(my_string)
    print(repr(my_string))
    print(len(my_string))
    print(my_string + my_string1)
    print(my_string == my_string1)
