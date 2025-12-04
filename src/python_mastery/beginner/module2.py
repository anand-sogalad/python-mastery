# Most use python built in data types
# Integers, floats, strings and booleans
#
# Integers: number without decimal point
number = 10

# floats: number with decimal point
decimal_number = 10.123

# strings: strings are immutable sequence of unicode charecters
string = "I am string"

# boolean: Boolean represent truthiness either true or false
true = True
false = False

# variables and assignment
# Variables are names that referes to data stored in a memory
#
# we use assignment operator to assign memory referece of an object/data to variable
#
# simple assigment
var = "I am string"

# multiple assignment
var1 = var2 = 10

# tuple unpacking
# this automatically assigns 1, 2, 3 to var1, var2, var3 respectively
var1, var2, var3 = 1, 2, 3

# Type castig: converting one type of data into another is type casting
number = 10  # int
string = str(number)  # converted to str

print(type(number), type(string))  # this outputs class <int>, class <str>

# operators: operators helps us to do some opertion on data
# Arithmetic operators: +, -, *, /, //, **, %
# Comparison operators: <, >, <=, >=, ==
# Logical operators: and, or, not
# Indentity operaore: is, is not
# Membershiio operators: in, not in
#
# Airthmetic operators used to perform arithmetic operations
print(1 + 1)
print(1 - 1)
print(1 * 1)
print(1 / 1)
print(1 // 1)
print(1 % 1)
print(1**1)

# comparsion operators used to compare values
print(1 == 1)
print(1 < 2)
print(1 <= 2)
print(2 > 1)
print(2 >= 1)

# logical operators used in with multiple comparison operators
print(1 == 1 and 1 < 2)  # True
print(1 == 1 or 1 != 1)  # True
print(not 1 != 1)  # True

# Indentity operators used to check if the object and its memory is same
string1 = "anand"
string2 = "anand"
string3 = string2

print(string1 is string2)  # This can be False
print(string2 is string3)  # This is True

# Membership operatrs use to check if the element present in the collection
print("a" in "anand")  # True
print("b" in "anand")  # False

# string concatination and repetation
# string supports both concatination and repeatation operation
# Note: concations works only between two strings and repeation works only between string and integer
#
# # concatination
print("anand" + "sogalad")  # becomes `anandsogalad`

# repeatation
print("anand" * 2)  # becomes `anandanand`
