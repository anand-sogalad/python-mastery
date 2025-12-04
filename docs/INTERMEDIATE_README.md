# PCAP Roadmap

---

## 📘 1. Modules and Packages (17%)

### Importing Modules
- `import module`
- `from module import name`
- Module aliasing (e.g., `import math as m`)
- Using `__name__ == "__main__"`

### Standard Library Modules
- `math`, `random`, `platform`, `datetime`
- Creating your own modules

### Packages
- Folder as package
- `__init__.py`
- Importing from packages

---

## 📗 2. Strings and List Processing (22%)

### String Operations
- Indexing, slicing
- Methods: `find()`, `join()`, `split()`, `replace()`, `startswith()`, `endswith()`, `is...()`
- Escape sequences, raw strings

### Lists
- List slicing
- List comprehensions
- Copying lists (shallow vs. deep)
- Sorting lists: `sorted()` vs `.sort()`
- List methods: `pop()`, `insert()`, `remove()`, `extend()`, etc.

### Tuples
- Tuple creation, indexing, immutability
- Packing/unpacking

---

## 📙 3. Functions (22%)

### Defining and Calling Functions
- Parameters, return values
- Default parameters
- Keyword arguments
- Arbitrary arguments: `*args`, `**kwargs`
- Lambda functions

### Recursion

### Closures
- Nested functions
- Returning functions

### Generators & Iterators
- `yield`
- `next()`
- Generator expressions

---

## 📕 4. Object-Oriented Programming (26%)

### Classes and Objects
- Creating classes
- `__init__` method
- Instance variables and class variables

### Methods
- Instance methods
- Class methods (`@classmethod`)
- Static methods (`@staticmethod`)

### Inheritance
- Single & multiple inheritance
- Overriding methods
- `super()` usage

### Encapsulation
- `_protected` and `__private` fields
- Name mangling

### Polymorphism
- Duck typing
- Method overriding

### Special Methods (Magic / Dunder Methods)
- `__str__`, `__repr__`, `__len__`
- `__add__`, `__sub__`, etc.
- `__iter__`, `__next__`
- `__eq__`, `__lt__`, `__gt__`

---

## 📔 5. Exception Handling (13%)

### Types of Exceptions
- Built-in exceptions
- Raising exceptions (`raise`)

### `try–except–else–finally`
- Multiple except blocks
- Exception hierarchy
- Custom exceptions

---

## 📒 6. File Processing (13%)

### Working with Files
- Opening files (`open()`)
- Reading: `read()`, `readline()`, `readlines()`
- Writing & appending
- File modes: `r`, `w`, `a`, `rb`, `wb`

### Working With Context Manager
- `with open() as f:`

### Working with binary files

---

## 📓 Extra Topics (Frequently Asked in PCAP)
- Mutable vs. Immutable types
- Python memory model & object lifecycle
- Iterables vs. Iterators
- Comprehension types: list, dict, set
- Using the `in` operator
- String formatting (`f-strings`, `format()`)
