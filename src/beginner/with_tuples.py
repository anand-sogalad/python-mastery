# Tuples are immutable data structure that store collection iof items. it is also ordered

if __name__ == "__main__":
    numbers = (-1, -10, 25, 43, 56, 43, 10, 5)

    # getting to know attributes and methods supprted by tuples
    print(dir(numbers))

    # iterating through tuple
    for item in numbers:
        print(item, end=" ")
    print()

    # using indexing
    for idx in range(len(numbers)):
        print(numbers[idx], end=" ")
    print()

    # using enumerate
    for idx, item in enumerate(numbers):
        print(idx, item, end=" ", sep="=")
    print()
