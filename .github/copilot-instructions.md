# Copilot Instructions for Python Mastery

## Project Overview
This is a structured Python learning repository following PCEP → PCAP → PCPP1 certification paths. The project is organized as a progressive curriculum with empty `src/` and `tests/` directories ready for hands-on practice implementations.

## Architecture & Organization

### Directory Structure
- `src/` - Main implementation code organized by certification modules
- `tests/` - Corresponding test files following the same module structure
- `README.md` - Comprehensive curriculum roadmap with checkboxes for progress tracking

### Module Organization Pattern
Follow the README.md structure when creating new modules:
```
src/
├── pcep/           # PCEP certification modules (fundamentals)
│   ├── module1/    # Intro & Basics
│   ├── module2/    # Data Types, I/O, Operators
│   ├── module3/    # Conditionals, Loops, Lists, Bitwise
│   └── module4/    # Functions, Recursion, Tuples, Dicts, Exceptions
├── pcap/           # PCAP certification modules (intermediate + OOP)
│   ├── module1/    # Modules, Packages, PIP
│   ├── module2/    # Strings, Lists, Exceptions
│   ├── module3/    # OOP
│   └── module4/    # Iterators, Generators, Files, Utilities
└── pcpp1/          # PCPP1 certification modules (advanced)
    ├── module1/    # Classes, Decorators, Abstract, Deep/Shallow Copy
    ├── module2/    # Inheritance, Polymorphism, Special Methods
    ├── module3/    # Advanced Exception Handling
    ├── module4/    # Pickle & Shelve
    └── module5/    # Metaclasses
```

## Development Conventions

### File Naming
- Use descriptive module names that reflect the learning objective
- Include both practice implementations and mini-projects in the same module
- Example: `pcep/module2/calculator.py`, `pcep/module2/unit_converter.py`

### Test Structure
Mirror the `src/` structure in `tests/` with `test_` prefix:
```
tests/pcep/module1/test_calculator.py
```

### Learning-Focused Implementation
- **Include docstrings** explaining the concept being demonstrated
- **Add comments** highlighting Python-specific features or gotchas
- **Implement multiple approaches** when demonstrating architectural decisions
- **Include performance comparisons** where mentioned in README.md mini-projects

### Practice Requirements
Each module should include:
1. **Basic Practice** - Simple implementations of core concepts
2. **LeetCode/HackerRank** - Algorithm problems (include problem URLs in comments)
3. **Mini-projects** - Architectural exploration as specified in README.md
4. **Examples** - Concrete code demonstrating "Good-to-Know" concepts

## Development Workflow

### Creating New Modules
1. Reference the README.md checklist for the specific module requirements
2. Create both `src/` and `tests/` directories for the module
3. Implement practice exercises first, then mini-projects
4. Include comprehensive docstrings explaining the learning objectives

### Code Style
- Follow PEP 8 conventions
- Use type hints for educational clarity
- Include performance profiling code where mini-projects mention it
- Document architectural decisions in mini-projects

### Dependencies
The .gitignore supports multiple package managers (pip, poetry, pipenv, pdm, pixi). Choose appropriate tools for different modules when learning dependency management.

## Key Patterns to Follow

### Educational Code Structure
```python
def demonstrate_concept():
    """
    Learning objective: [specific concept being taught]
    
    This function demonstrates [key Python feature] and highlights
    [specific gotcha or best practice].
    """
    # Implementation with educational comments
```

### Mini-Project Architecture
Focus on the architectural exploration mentioned in README.md:
- Performance comparisons (use `timeit`, `sys.getsizeof`)
- Memory profiling implementations
- Framework design patterns (especially for PCPP1 modules)
- Production-ready error handling and logging patterns

This is a learning repository - prioritize clarity, comprehensive examples, and architectural exploration over production optimization.