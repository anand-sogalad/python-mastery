# In python conditional statements are meant to control the flow the program
# Lets evalualte conditaion statements along with some operators
#
# Comaparision operators:
#   ==, <, <=, >, >=
#
# Logical operators:
#   and, or, not
#
# Membership operators:
#   in, not in
#
# Idenity operaotrs:
#   is, is not


def get_input(msg: str):
    return input(f"{msg}: ")


def is_java(lng: str):
    return lng.lower() == "java"


def is_python(lng: str):
    return lng.lower() == "python"


if __name__ == "__main__":
    language = get_input("What is the programming language you know?")
    if is_java(language):
        print("You are Java Programmer!")
    elif is_python(language):
        print("You are Python programmer!")
    else:
        print(f"Sorry! we dont know about this language: {language}")
