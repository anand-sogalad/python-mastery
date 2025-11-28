# python do suport 2 different loops
# for loop and while loop
# for loop is used when we know how many iterations to be iterated
# while loop is used if iteration is needed util condition is met

if __name__ == "__main__":
    fruites = ["apple", "banana", "kiwi", "chikku", "orange", "papaya"]
    for fruit in fruites:
        print(fruit, end=" | ")
    print()

    for i in range(10):
        for j in range(10):
            print((i, j), end=" | ")
        print()

    while True:
        satisfied = input("are you satisfied with what you have? Y/N: ")
        if satisfied.lower().startswith("y"):
            print("Chill maddu!!!")
            break
        print("Work harder until you become satisfied!")
