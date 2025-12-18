from typing import Any, List

# Functions

# functions are block of code that are used for reusability
# In python we define function using def keyword
# there are differnt variations of functions available


# function without input and output
def without_input_wihout_output():
    print("I am funbction without input and output")


# function with input and without output
def with_input_without_output(input: str):
    print(f"I am function with input: {input} and without output")


# function without input and with output
def without_input_with_output():
    return "I am function without input and with output"


# function with input and output
def with_input_and_output(input: str):
    return f"I am function with input: {input} and output"


if __name__ == "__main__":
    without_input_wihout_output()
    with_input_without_output("Hello, I am input")
    print(without_input_with_output())
    print(with_input_and_output("Hello, I am input"))

# different types of arguments
# positional arguments : these arguments value are decided by their position
# positional arbitary arguments : these arguments values also decided by their postion
# keyword arguments : these value are decided by the name of the argument and position doesn't matter
# keyword arbitary arguments: these are decided by theier argument name not by postion
# default arguments: the arguments which has default value already set during function definition


# positional arguments
def function1(var1: int, var2: int, var3: str, var4: List[Any]):
    print(var1, var2, var3, var4)


# postional arbitary arguments
def function2(*args: Any):
    print(*args)


# keyword arguments
def function3(var1: Any, var2: Any):
    print(var1, var2)


# keyword arbitary arguments
def function4(**kwargs: Any):
    print(**kwargs)


# default arguments
def function5(var1: Any, var2: Any, var3: str = "I am default value"):
    print(var1, var2, var3)


if __name__ == "__main__":
    function1(
        1, 2, "str", [1, 2, 3]
    )  # based on the position the value will be assigned to respective vcariables
    function2(1, 2, 3, 4, 5, 6, 7)  # you can pass n number of arguments in to arbitary args
    function3(
        var2="X", var1="Y"
    )  # if you see here, position doesnt matter, only argument name matters
    function4(var1="X", var2="Y", var3=10)  # you can send as many as keyword arguments like this
    function5(
        1, 2
    )  # here I am not passing any value to var3, if not passed it takes default value. this is called default argument

# scope
# Local scope: a variable define inside an function is called local scope and local variable
# Global scope: a varibale defined at module is called global scope and global variable

# LEGB is the python lookup order for variables
# Local, Enclosing, Global, Built-in

# To modify the global at local scope we should use global keyword
# To modify the enclosing scoped variable in local scope we need to use nonlocal keyword


# Built-in function
# len() - this is used to get the length of an item
# type() - used check the data type of variable
# abs() - this return abs value of number
# round() - always prvides the rounded value
# min() - returns the smallest value
# max() - returns the highest value

if __name__ == "__main__":
    data = [1, 2, 4, 4, 5, 6]
    print(len(data))
    print(type(data))
    print(abs(data[-1]))
    print(round(12.567))
    print(min(data))
    print(max(data))
