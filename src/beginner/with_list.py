# List: List is a built in data structure in python.
#       It is ordered, mutable and collection of any data types


if __name__ == "__main__":
    # working with lists
    courses = ["Mathematics", "History", "Science", "English", "Kannada"]

    # getting the length of the list
    total_courses = len(courses)
    print(f"Total courses present in 'courses' list: {total_courses}")

    # getting the elements of a list using indexing
    item1 = courses[0]  # this return first element in the list
    item2 = courses[1]  # this return second element in the list
    # item3 = courses[10]  # this would raise an IndexError

    print(f"First and second item in the list are {item1}, {item2}")

    # python also supports negetive indexing
    first_item_from_last = courses[-1]  # get the first item from the last
    second_item_from_last = courses[-2]  # get the second item from the last

    print(f"printing Items from last, last 2 items: {first_item_from_last}, {second_item_from_last}")

    # modyfing list, list methods
    numbers = [0, 1, 2, 3, 4, 5]

    print(f"numbers list before any operations: {numbers}")

    numbers.append(6)  # this appends value to list to last index
    print(f"Appended 6 to numbers list: {numbers}")

    numbers.extend([7, 8, 9, 10])  # this appends list of values to the end of the list
    print(f"extending the list by appending list of elements [7, 8, 9, 10] to numbers list: {numbers}")

    numbers.insert(5, 100)  # this insert the value 100 at a given index 5
    print(f"Inserted 100 into 5th index of numbers list: {numbers[5]} at {numbers.index(numbers[5])}th index")

    retured = numbers.pop()  # this removes the last item in the list
    print(f"Last item of a list {retured} has been removed: {numbers}")

    returned = numbers.pop(5)  # this removed item from 5th index
    print(f"Item from 5th index is {returned} has been removed: {numbers}")

    numbers.remove(5)  # this removed the given item from the list
    print(f"Item 5 has been removed from the list: {numbers}")

    # we can also use del keyword
    del numbers[2]  # this deletes the item from the list

    print(f"this is ithe final state of a list : {numbers}")

    # sorting operations
    numbers.sort()  # this does in place sorting
    print(f"numbers list after sorted: {numbers}")

    numbers.sort(reverse=True)
    print(f"numbers list after sorted in reversed order: {numbers}")

    numbers.reverse()  # this does in place sort and reverse
    print(f"numbers: reversed list : {numbers}")

    # if we would like to preserve the state of the original list
    # we should make use of sorted and reversed built in functions
    numbers = [9, 0, 4, 6, -1, 2, 5, 7, 6, 8]
    print(f"The origional list: {numbers}")

    print(f"sorted list: {sorted(numbers)}")
    print(f"reversed list: {list(reversed(numbers))}")

    print(f"The origional list: {numbers}")

    # there are some more data processing built in functions
    print(sum(numbers))
    print(min(numbers))
    print(max(numbers))

    # iterating through list
    for item in numbers:
        print(item, end=" ")
    print()

    # iterating using indexing
    for idx in range(len(numbers)):
        print(numbers[idx], end=" ")
    print()

    # we can also iterate through and get their index values as well
    for idx, item in enumerate(numbers):
        print((idx, item), end=" ")
    print()
