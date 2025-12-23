# working with files


if __name__ == "__main__":
    file = "src/python_mastery/intermediate/module6.py"
    with open(file) as f:
        data = f.read()
    print(data)

    with open(file) as f:
        data = f.readlines()
        print(data)

    with open(file) as f:
        data = f.readline()
        print(data)

    with open(file) as f:
        for data in f:
            print(data)
