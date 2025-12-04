# Data collections: Lists, Tuples, Strings, Dictionaries, Sets
# Pythons built in data sturcutures are List, Tuple, Set and Disctionary
#
# Strings: Strings are immutable sequence of unicode charecters.
# As said, strings are sequencial and ordered. hence suports indexing adn slicing
# Lets look into them along with most common string methods
#
# Indexing: syntax: variable[inex]
string = "I am string"
print(f"1st char of a string: {string[0]}")
print(f"2nd char of a string: {string[1]}")
print(f"last char of a string: {string[-1]}")  # python support negetive indexing as well

# Slicing: syntax: variable[start_index:end_index:step_size]
# Slicing is used get a part of a string
# here sart index is -5 = t, end index not given which means, its set to end of the index
# step also not given, which means step is 1 by default
print(f"Last 5 chars of a string: {string[-5:]}")
print(f"First 5 chars of a string: {string[:5]}")  # starting from 0 to 4 indexes. 5 is excluded
print(f"Reversed: {string[::-1]}")  # slicing is used for reversing as well

# lets look at some most commonly used string methods
print(string.upper())  # return new string in upper case
print(string.lower())  # returns new string in lower case
print(string.find("a"))  # return smallest index of a given sub string
print(string.replace("a", "s"))  # replaces with new string
print(string.split())  # converts to list

# list: list is ordered collection of items and mutable data structure in python
# it can store any data type
items = ["CD", "DVD", 10, 15, "Car", "Elephent", (1, 2, 3), [1, 2, 3], {1, 2, 3}, {1: 2, 2: 3, 3: 4}]
print(f"1st element: {items[0]}")
print(f"Last item: {items[-1]}")
print(f"Last 3 items: {items[-3:]}")
print(f"First 2 items: {items[:2]}")
print(f"List reversed: {items[::-1]}")

# commonly used slist methods
items.append(10)  # adds this item to list to last index
items.extend([123123, 231231, 23123, 1213])  # adds multiple items to the list
items.remove(10)  # remove the given vale if found else raises ValueError
items.pop()  # removes and returns last item in the list
items.pop(1)  # removes item from 1st index and returns
items.sort()  # sorts the list in place
items.reverse()  # reverse the list in place
items.count(10)  # counts the number of occeurences of given item in a list
items.index(5)  # return smallest index of a given value, otherwise ValuError

print(len(items))  # return the length of the list
print(reversed(items))  # returns new list that reversed
print(sorted(items))  # returns new sorted list

# Tuples: Tuples are very similer to list, but unlike list, they are immutable
tuple_items = (1, 2, 3, 4, 5)
print(len(tuple_items))
var1, var2, var3, var4, var5 = tuple_items  # Tuple unpacking

# Dictionaries
# Dictionaries are data structures in python, they are ordered and key and value pairs
dictionary_items = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

# most commonly used methods
dictionary_items.update({6: "Six", 7: "Seven"})  # inserting/updating dictionary
dictionary_items.get(1)  # accessing value
dictionary_items.setdefault(10, "")  # inserts key with default value
dictionary_items[1] = "ONE"  # Updating value
dictionary_items.pop(1)  # removes key and retuns value
dictionary_items.popitem()

del dictionary_items[10]

dictionary_items.keys()
dictionary_items.values()
dictionary_items.items()
dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9])


# Set: Set is collection of hashable values/items
# Set is mutable and store only unique values/items
items_set = {1, 2, 3, 4, 5}

items_set.add(10)  # add the value to set
items_set.update({1, 2, 3, 4, 5, 6, 7, 10})  # adds the values to set
items_set.pop()  # remove value and returna it
items_set.remove(10)  # removes the value from set
