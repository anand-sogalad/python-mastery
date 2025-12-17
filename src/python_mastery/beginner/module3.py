# Control flow - conditions and loops

# conditional statements
# python uses `if`, `elif`, `else` keywords for writing conditional statements
# these conditional statements help to control the flow of a program

# examples
if __name__ == "__main__":
    # example 1
    raining = True
    if raining:
        print("Let's take umbrella")
    else:
        print("Let's not take umbrella")

    # example 2
    day = "Monday"
    if day == "Monday":
        print("Let's go to school")
    elif day == "Tuesday":
        print("Let's go to temple")
    else:
        print("Let's go to vacation")

    # example 3
    day = input("Enter what day today: ")
    match day:
        case "Monday":
            print("It's a monday")
        case "Tuesday":
            print("It's Tuesday")
        case _:
            print("It's someday")

# Looping statements
# Looping statements helps to iterate over same block of code again and again
# There are 2 different loops in python
# for loop: this loop is used when we know how many iterations needed
# while looop: this loop is used when we know, until which condition iteration needed

if __name__ == "__main__":
    # example 1 - iterate 10 times
    for i in range(10):
        print(i, end=" ")
    print()

    # example 2 - iterate until value becomes 0
    value = 100
    while value != 0:
        print(value, end=" ")
        value //= 2
    print()

    # iterating through collection
    collection = ["apple", "mango", "banana", "straberry"]
    for item in collection:
        print(item, end=" ")
    print()

    # iterating through strings
    my_string = "I am being iterated"
    for string in my_string:
        print(string, end="")
    print()

    # with break, continue and pass statements
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for item in items:
        if item == 5:
            continue
        if item % 10 == 0:
            break
        print(item, end=" ")
    print()
