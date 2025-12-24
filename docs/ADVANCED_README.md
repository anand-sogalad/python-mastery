# PCPP1 Roadmap

**Exam Code:** PCPP-32-101  
**Level:** Professional  
**Focus:** Advanced Python, real-world programming, architecture concepts

**Exam Structure:**
- 5 Sections
- 45 Questions
- Heavy emphasis on OOP, decorators, networking, GUI, file & DB work

*(Source: Official OpenEDG / Python Institute syllabus)*

---

## 📘 1. Advanced Object-Oriented Programming (35%)

### OOP Foundations (Deep Level)
- Class, object, instance, attribute, method
- Instance vs class variables
- `__init__`
- `isinstance()`, `issubclass()`

### Python Core Syntax via Magic Methods
- Comparison: `__eq__`, `__lt__`, `__gt__`
- Numeric: `__abs__`, `__add__`, etc.
- Type conversion & introspection:
  - `__str__`, `__repr__`
  - `__getattr__`, `__getitem__`
- Extending syntax behavior using dunder methods

### Inheritance, Polymorphism & Composition
- Class hierarchies
- Single vs multiple inheritance
- MRO (Method Resolution Order)
- Duck typing
- Inheritance vs composition
- "is-a" vs "has-a" modeling

### Advanced Function Arguments & Decorators
- `*args`, `**kwargs`
- Argument forwarding
- Closures
- Function decorators
- Class decorators
- Decorators with parameters
- Decorator stacking
- `__call__`

### Static & Class Methods
- `@staticmethod`
- `@classmethod`
- `cls` usage
- Factory patterns via class methods

### Abstract Base Classes
- `abc` module
- Abstract classes & methods
- Overriding abstract methods
- Multiple inheritance with ABCs

### Encapsulation
- Getters, setters, deleters
- Attribute protection strategies

### Subclassing Built-in Types
- Extending `list`, `dict`, `str`, etc.
- Modifying built-in behavior

### Advanced Exception Handling
- Exception objects & attributes
- Exception chaining
- `__context__`
- `__cause__`
- Tracebacks (`__traceback__`)

### Shallow vs Deep Copy
- Identity vs value vs reference
- `id()`, `is`
- `copy()` vs `deepcopy()`

### Serialization & Persistence
- `pickle`
- `shelve`
- `dumps()` / `loads()`
- Object persistence concepts

### Metaprogramming
- Metaclasses
- `type()`
- Special attributes:
  - `__class__`, `__bases__`, `__dict__`
- Runtime class manipulation

---

## 📗 2. Coding Best Practices & Design Patterns

### PEP 8 & Style Guidelines
- Code layout and formatting
- Naming conventions
- Documentation strings
- Code comments

### Design Patterns
- Common design patterns in Python
- Creational patterns
- Structural patterns
- Behavioral patterns

---

## 📙 3. GUI Programming & Event-Driven Development

### GUI Frameworks
- `tkinter` basics
- Event-driven programming
- Widgets and layout management
- Event handlers

### GUI Components
- Windows, buttons, labels
- Text entry, checkboxes, radio buttons
- Menus and dialogs

---

## 📕 4. Network Programming & RESTful APIs

### Network Basics
- Sockets
- Client-server architecture
- TCP/IP basics

### HTTP & REST
- HTTP methods (GET, POST, PUT, DELETE)
- RESTful API design
- JSON data exchange
- API authentication

### Python Networking Libraries
- `socket` module
- `requests` library
- `urllib` module

---

## 📔 5. File Processing & Database Operations

### File Handling
- Binary vs text files
- File modes and operations
- Context managers (`with` statement)
- File iteration

### Database Operations
- Database concepts
- SQL basics
- Python DB API
- `sqlite3` module
- CRUD operations
- Transactions and error handling
