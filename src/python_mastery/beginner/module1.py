# Computing and Programming Basics

# What is a computer program?
# A computer program is a set of instructions that instructs computer to perform specific actions


# Interpreters vs Compilers (wrt python)
# An interpreter is program/software that executes python code line by line
# A compiler is program/software that translates python code into bytecode


# Python language charecteristics
# Python is interpereted, dynamically typed and general perpose programming language

# Python charecteristics are:
# Python has simple syntax
# Python is portable
# Python supports multiple programming paradigms such as procedural, functional and oop
# Python has large standard library
# Python is cross platform supported
# Python is dynamically typed
# Python is interpreted


# How python executes code
# Pythons, first compiles the code into byte code using compiler
# The translated code is stored in .pyc file
# And, .pyc file is executed by python interpreter (pvm - python virtual machine) line by line


# Python keywords, indentifiers and variables
# Python keywords are reserved words with predefined meaning to them. we cannot use them as identifiers
# Python idetifiers are name of any entity in python such class, function, module, variables etc...
# Python variables are names that referes to a value stored in a memory
# Not all identifiers are variables but all variables are idenifiers


# Python Execution Model

# How to run python scripts?
# There are many ways to run python scripts
# 1. run as a script
# 2. run as a module
# 3. run in interactive mode

# when this file - module1.py is executed using `python module1.py` command
# everything within the `if __name__ == "__main__":` block get executed
# that is because when the file itself is executed, the file name becomes `__name__` otherwise it have module name (file name itself)

number = 15
name = "First Last"

if __name__ == "__main__":
    print(name, number)


# Basic Syntax and Structure

# Indentation rules
# python follows the `4 spaces` as indentation that is used to define block of code unlike braces {} in java and c


# Comments in python
# Python support single and multiline comments
# this is a single line comment
"""
This is a multiline comment
in Python
"""


# Naming conventions
# Python follows PEP8 for coding guidelines for writing readbale and maintainle code
# as per PEP8,
# variables functions and modules must use snake_case
# constants must use SNAKE_CASE
# package names must be simple and single word otherwise use snake_case or lower
# class names numst use CamleCase
