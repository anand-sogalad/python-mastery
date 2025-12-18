# Data collections - Lists, Tuples, Strings, Dictionaries

# Strings: Strings are immutable sequence of unicode charecters, once they created they cannot be modified

# indexing: Indexing is the process of extracting an element from a specific index of an item
string = "012345"

if __name__ == "__main__":
    print(string[0], end=", ")  # extracting 0th index
    print(string[4], end=", ")  # extracting 4th index
    print(string[-1], end=", ")  # extracting item from last index

# slicing: slicing is the process of extracting a part of the item
if __name__ == "__main__":
    print()
    print(string[:-1])  # extracting substring from 0th to last (excluded)
    print(string[2:-1])  # extracting substring from 2th to last (excluded)
    print(string[::-1])  # reversing a string

# Most used string methhods
string = "i am a string used for testing"

if __name__ == "__main__":
    print(f"convert to upper case: {string.upper()}")
    print(f"covnert to lower case: {string.lower()}")
    print(f"check if the string is lower: {string.islower()}")
    print(f"check if the string is upper: {string.isupper()}")
    print(f"Check if the substring present: {string.find('am')}")
    print(f"convert to title: {string.title()}")
    print(f"capitalize 1st letter of a string: {string.capitalize()}")
    print(f"Convert to list: {string.split()}")
    print(f"replace am with are: {string.replace('am', 'are')}")


# Lists: List is data structure in python used to store any data. it is ordered and mutable data structure

# Indexing and slicing concepts remains same as string

# Most used list methods
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":
    items.reverse()
    print(f"items got reversed: {items}")

    items.sort()
    print(f"items got sorted: {items}")

    print(f"total {items.count(10)} count of 10 are present in {items}")
    items.index(10)
    items.append(11)
    items.extend([12, 13, 14, 15])
    print(items)


# Tuples: Tuples are data structures used store any data typpe but unlike list they are immutable

# indexing and slicing work as same as sting/list
tuple_items = (1, 2, 3, 4, 5)

# tuple methods
if __name__ == "__main__":
    print(tuple_items.count(1))
    print(tuple_items.index(1))
