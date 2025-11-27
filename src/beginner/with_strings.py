from time import perf_counter

str1 = "Simple String"
str2 = "Simple's String"
str3 = 'I can be anything but "Dangerous"'
multi_line = """I am going to Bengaluru.
I can be anywhere!"""

if __name__ == "__main__":
    # just iterating through strings and printing them
    strat_time = perf_counter()
    for item in str1, str2, str3, multi_line:
        print(item)
    print(f"Time taken to complete the loop: {perf_counter() - strat_time:2f}s")

    # getting the len of a string
    print(f"Length of str1 is {len(str1)}")

    # iterating over a string for char
    for char in str1:
        print(char)

    # iterating over a string for char, but by indexing this time
    for i in range(len(str1)):
        print(str1[i])

    # string indexing
    print(str1[1])  # getting second char

    # string slicing
    print(str1[:2])  # getting substring up to inde 1
    print(str1[-2:])  # getting last 2 cahars sub string
    print(str1[::-1])  # string reversing

    # string methods
    print(str1.lower())  # converting to lower case
    print(str1.upper())  # conerting to uppercase
    print(str1.capitalize())  # convert to first letter to capital
    print(str1.title())  # converting to title, eavery words fist letter is upper case
    print(str1.isalnum())  # checking if the string contains alphabets and numbers
    print(str1.isalpha())  # checking if the sring has only alphabets
    print(" ".isspace())  # checking if the string is space

    # this counts the given sub string in a string and returns int value
    print(str1.count("i"))

    # finding the index of the substring in a string
    print(multi_line.find("I"))

    # if not found returns -1
    print(multi_line.find("z"))

    # we can find using index as well
    print(multi_line.index("I"))

    # but if not found this raises ValueError
    try:
        print(multi_line.index("z"))
    except ValueError:
        print("Given string not found")

    # replace a substring, as string is immutable it returns new string object
    print(str1.replace("Simple", "Best"))

    # cancatinating string
    hello: str = "Hello"
    name: str = "Bob"
    greeting: str = hello + name
    print(greeting)

    greeting: str = hello + " " + name
    print(greeting)

    using_f_string = f"{hello} {name}"
    print(using_f_string)

    # built in function dir() helps to get an object's attributes and methods
    print(dir(using_f_string))
