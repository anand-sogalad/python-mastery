import random


# Functions
# Functions are block of code that can be resued and they are defined using def keyword
#
# There are different variations of functions
#
# function with no arguments and no return value
def func():
    print("I am func")


# function with argument and no return value
def func1(msg: str):
    print(f"func1 takes 1 argument `msg` and its value is {msg}")


# function without argument and return value
def func2():
    return random.randint(1, 100)


# function with argument and return value
def func3(msg: str):
    return f"Your message is {msg}"


# types of arguments
# positional arguments: as name suggests, position of the argument matters.
def add(a, b):
    return sum([a, b])


# keyword arguments
def add1(a, b):
    return sum([a, b])


# default arguments
def add2(a: int, b: int, c=10):
    return sum([a, b, c])


# arbitary positional arguments (by convinient we use *args for arbitary arguments)
def add3(a, b, *args):
    return sum([a, b, *args])


# arbitary keyword arguments (by convinient we use **kwargs for keywords arbitary arguments)
def personal_info(name, age, **kwargs):
    return {"name": name, "age": age, **kwargs}


# let's discuss about scope now
# In python, look up orders is LEGB = local > Enclosing > Global > Built in

a = "global scope"


def func_legb():
    b = "enclosing scope"

    def func():
        b = "local scope"
        print(b)  # this prints 'local scope'

        print(b)

    func()
    print(b)
    global a
    a = "modified"  # global 'a' is modified
    print(a)


if __name__ == "__main__":
    result = add(1, 2)  # first value assigned a and second is to b automatically based on the position
    result = add1(b=1, a=1)  # when you specifically use argument name and assign value, position doesnt matter.
    result = add2(1, 2)  # here, we are passing only 2 prguments, as 2rd argument alerdy assigned default value
    result = add2(1, 2, 3)  # here the default argument has been over ridden

    # when we dont know how many parameter should be passed to function,
    # we can simple use positional arbitary argument
    result = add3(1, 2, 3, 4, 5, 6, 7, 8)  # a, b got 1st 2 postions, next all are assigned to args
    print(result)  # 36

    result = personal_info("anand", 10, address="Bengaluru", city="Bengaluru", phone="888-000-00-00")
    print(result)  # {'name': 'anand', 'age': 10, 'address': 'Bengaluru', 'city': 'Bengaluru', 'phone': '888-000-00-00'}

    func_legb()
    print(a)  # this prints 'modified'

    print(len([1, 2, 3]))  # used to print lenth of an object
    print(type(a))  # used to print data type of an object
    print(abs(-123))  # this is to print absolute value of an numeric value
    print(round(123.1234, 2))  # it rounds off a given numeric value, here after decimal point 2 digits accepted
    print(min([1, 2, 3, 5]))  # prints the smallest item of an iterable
    print(max([1, 2, 3, 4, 5]))  # prints the largest item of iterable
