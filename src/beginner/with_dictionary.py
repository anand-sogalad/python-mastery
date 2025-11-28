# Dictionaries is python are data structure
# that contains key and value paris
# key are are always unique and oredered
# and mutable data structure

if __name__ == "__main__":
    # create a empty disctionary
    data = {}

    # add key and value to dictionary
    data["name"] = "Anand Sogalad"
    print(f"Updated disctionary : {data}")

    # adding multiple key value pairs
    data.update({"age": 35, "qualification": "Not applicable"})
    print(f"Updated the dictionary again : {data}")

    # list of avaialable attributes and methods
    print(dir(data))

    for key in data:
        print(key, data[key], end=" | ")
    print()

    for key in data.keys():
        print(key, data[key], end=" | ")
    print()

    for value in data.values():
        print(value, end=" | ")
    print()

    for key, value in data.items():
        print((key, value), end=" | ")
    print()
