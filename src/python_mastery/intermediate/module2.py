import copy
from typing import Any, List

# String and List processing

# Indexing, Slicing
# Indexing the process of getting a element from a siungle index where is slicing the process of extracting sub section of the intems such as string or lists

# String mehods
my_string = "abcdef ghijklmn"

if __name__ == "__main__":
    # find the index of a sub string in a string
    # find the method returns -1 if item not found
    print(my_string.find("n"))
    print(my_string.find("o"))

    # join the list into string
    print("".join(["I", " ", "am", " ", "abcdef"]))

    # split is used to convret string in to list
    print(my_string.split())

    # replace a string or substring with another
    print(my_string.replace("abcdef", "xyzabc"))

# list methods
my_list: List[Any] = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    # shallow copy vs deep copy
    # Shallow copy copies the object and keeps the internal refence as is where as deep copy is
    # copies of internal objects as well and create different refences to it

    new_list = copy.copy(my_list)
    print(id(my_list))  # print different id
    print(id(new_list))  # prints different id

    print(id(my_list[0]))  # prints same id
    print(id(new_list[0]))  # prints same reference

    new_deep_copy_list = copy.deepcopy(my_list)

    print(id(my_list))  # print different id
    print(id(new_deep_copy_list))  # prints different id

    print(id(my_list[0]))  # prints differnt id
    print(id(new_deep_copy_list[0]))  # prints differnt id

    # sorting list
    print(sorted(my_list))
    my_list.sort()
    print(my_list)

# samething can be done for tuples except that it cant be modified and doesnt support much of methods
