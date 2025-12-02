# conditional statements
# `if
# if-else
# if-elif-else`

# Conditional statements used for controlling the flow of program based on the conditions
#
# use case: go for walk if not raining else be at home
if input("Is it raining? ").lower().startswith("y"):
    print("let's be at home and watch weather news")
else:
    print("Let's go for walk!")

# use case if elif and else
# use case: if monday to friday go to school, if sunday go to play cricket otherwise be at home
weekday = input("What is the weekday today? ").strip().lower()
if weekday == "sunday":
    print("Let's go to play cricket")
elif weekday == "saturday":
    print("Let's be at home today")
else:
    print("let's go to school")

# lately python also started supporting match case like switch in other languages
# match case is better if there are many conditions to be checked
number = input("Enter number within 1 to 5 (both inclusive) ")
match number:
    case "1":
        print("You entered ONE")
    case "2":
        print("You entered TWO")
    case "3":
        print("You ENTERED THREE")
    case "4":
        print("You entered FOUR")
    case "5":
        print("You entered FIVE")
    case _:
        print("Wrong input!")


# looping statements
# for loop and while loop: for loop is used when weknow iterations to be looped and while loop is used when we know only the condition
#
# for loop
for i in range(10):
    print(i)

# iterating through list
for item in ["abc", "def", "ghi", "jkl"]:
    print(item)

# iterating through string
for char in "i am testing something":
    print(char)

# while loop
start = 0
end = 10
while start < end:
    print(start)
    start += 1

# using loop control statements
for i in range(15):
    if i % 3 == 0:
        continue
    if i % 2 == 0:
        pass
    if i % 5 == 0:
        continue
    print(i)
