# Data collections - Lists, Tuples, Strings, Dictionaries

# Strings: Strings are immutable sequence of unicode charecters, once they created they cannot be modified

# indexing: Indexing the process of extracting an element from a specific index of an item
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
