import pytest
from src.pcep.module2.practice import Addition, Person

"""
Unit tests for Person and Addition classes in pcep/module2/practice.py

Learning objective: 
- Test encapsulation, property validation, and operator overloading in Person.
- Test operator overloading and type handling in Addition.
"""


class TestPerson:
    def test_person_initialization_and_weight_property(self):
        p = Person("Alice", 30, 70)
        assert p.weight == 70

    def test_person_weight_setter_valid(self):
        p = Person("Bob", 25, 50)
        p.weight = 99
        assert p.weight == 99

    def test_person_weight_setter_invalid_low(self):
        p = Person("Carol", 40, 50)
        with pytest.raises(ValueError):
            p.weight = 0

    def test_person_weight_setter_invalid_high(self):
        p = Person("Dave", 35, 50)
        with pytest.raises(ValueError):
            p.weight = 101

    def test_person_add_operator(self):
        p1 = Person("Eve", 20, 60)
        p2 = Person("Frank", 22, 30)
        assert (p1 + p2) == 90


class TestAddition:
    def test_addition_with_ints(self):
        a = Addition(5)
        b = Addition(7)
        assert (a + b) == 12

    def test_addition_with_floats(self):
        a = Addition(2.5)
        b = Addition(3.5)
        assert (a + b) == 6.0

    def test_addition_with_strings(self):
        a = Addition("hello")
        b = Addition("world")
        assert (a + b) == "hello world"

    def test_addition_type_error(self):
        a = Addition(5)
        b = Addition("oops")
        with pytest.raises(TypeError):
            _ = a + b
