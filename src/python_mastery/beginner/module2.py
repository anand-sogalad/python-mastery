# Data Types, Variables, Basic I/O

# Built-in Data Types
# Python's built-in data types are
# int, float, str, bool
INT = 15  # this represents whole number
FLOAT = 15.15  # this represents whole number with decimal point
STR = "I am string"  # this represent sequesnce of chars (string)
BOOL = True  # this represent truthyness either True or False

# let's print the value and its type on the screen
if __name__ == "__main__":
    print(
        f"{INT} - {type(INT)}",
        f"{FLOAT} - {type(FLOAT)}",
        f"{STR} - {type(STR)}",
        f"{BOOL} - {type(BOOL)}",
        sep="\n",
    )


# Variables and Assignments
# Variables are names that referes to a value stored in a memory
# we can use variable to assign value to it, nothing but it referes to memory that value stored in

simple_assignment = 10  # single reference for a value
var1 = var2 = 10  # multiple references for a same value
var3, var4, var5 = 3, 4, 5  # multiple value to multiple reference in a single line
var6, var7, var8 = (6, 7, 8)  # same like above, but this tuple unpacking


# Type casting
# Type casting is a process of converting one data type to another data type
INT_FLOT = float(INT)  # this convert int to float
FLOAT_INT = int(FLOAT)  # this convert float to int
STR_INT = int("10")  # this conver str to int


# Using input() and print()
# print() and input() are built-in functions in python
# print() is used to output a result to screen/terminal
# input() is used take input from a screen/terminal

if __name__ == "__main__":
    name = input(
        "Please enter your name: "
    )  # this takes input from user entered value on screen terminal
    print(f"You entered `{name}`")  # this produces output to terminal/screen


# Operators
# Arithmetic operators # works on numbers
# Logical operators # works with multiple conditional statements
# Comparison operators # used to compare operands
# Bitwise operators # user to operate on bits
# Membership operators # use to check a value in an item
# Identity operators # used to check object identity

# Arithmetic operators
if __name__ == "__main__":
    print(f"Arithmetic operation: {5 + 5}")
    print(f"Subtraction operation: {10 - 5}")
    print(f"Division operation: {10 / 2}")
    print(f"Floor division operation: {10 // 3}")
    print(f"Multiplication operation: {10 * 2}")
    print(f"Exponention operation: {10**2}")
    print(f"Modulus operation: {10 % 2}")

# Comparison operators
if __name__ == "__main__":
    print(f"10 > 9 : {10 > 9}")
    print(f"9 < 10 : {9 < 10}")
    print(f"10 >= 9 : {10 >= 9}")
    print(f"9 <= 10 : {9 >= 10}")
    print(f"10 == 10 : {10 == 10}")
    print(f"10 != 9 : {9 != 10}")

# Logical operators
if __name__ == "__main__":
    print(f"True and False : {True and False}")
    print(f"True or False : {True or False}")
    print(f"not False : {not False}")

# Membership operators
if __name__ == "__main__":
    print(f"a in abc : {'a' in 'abc'}")
    print(f"a not in abc : {'a' not in 'abc'}")

# Identity operators
if __name__ == "__main__":
    a = 10
    b = 10
    print(f"a is b : {a is b}")
    print(f"a is not b : {a is not b}")

# String operators
if __name__ == "__main__":
    print(f"a + a : {'a' + 'a'}")  # concatination
    print(f"a * 10 : {'a' * 10}")  # repeatation
