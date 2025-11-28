# sets are mutable, unordered data structure used to store unique elements

if __name__ == "__main__":
    my_set = set()  # create empty set

    print(f"Here is a empty set: {my_set}")

    my_set.add("Sunday")
    print(f"after adding an item, the set: {my_set}")

    my_set.update([1, 2, 3, 4, 5])
    print(f"added multiple ites, the set: {my_set}")

    my_set.remove(5)  # removing given item from the sdet, keyError if no value found
    my_set.discard(5)  # removes the given item, no key error if not found
    my_set.pop()  # removes randomly

    my_set.clear()  # clears entier set
    print(my_set)
