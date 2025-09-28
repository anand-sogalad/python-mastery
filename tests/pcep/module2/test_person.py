import pytest
from src.pcep.module2.practice import Person

"""
Unit tests for Person class in pcep/module2/practice.py

Learning objective: Testing class encapsulation, property, setter validation, and operator overloading.
"""


class TestPerson:
    def test_person_initialization_and_weight_property(self):
        p = Person("Alice", 30, 70)
        print("person's weight is", p.weight)

    def test_person_weight_setter_validation(self):
        p = Person("Bob", 25, 50)
        # The setter should raise ValueError for out-of-range weights
        with pytest.raises(ValueError):
            p.weight = 0
        with pytest.raises(ValueError):
            p.weight = 101

    def test_person_add_operator(self):
        # Since weight property is broken, __add__ will also fail
        p1 = Person("A", 20, 60)
        p2 = Person("B", 22, 50)
        total_weight = p1 + p2
        print("total weight of p1 and p2 is", total_weight)
