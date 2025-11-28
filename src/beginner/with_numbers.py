# int is a whole number without any fraction part
# float is number with fraction part


# Arithmetic operators
# Addition
# Subtraction
# Multiplication
# Division
# Floor Division
# Exponention
# Modulus

if __name__ == "__main__":
    num1 = 10
    num2 = 5

    # addtion
    num3 = num1 + num2
    print(f"Addition: {num3}")

    # subtaction
    num3 = num1 - num2
    print(f"Subtraction: {num3}")

    # multiplication
    num3 = num1 * num2
    print(f"Multiplication: {num3}")

    # division
    num3 = num1 / num2
    print(f"Division: {num3}")

    # floor division
    num3 = num1 // num2
    print(f"Floor Division: {num3}")

    # exponention
    num3 = num1**num2
    print(f"Exponention: {num3}")

    # modulus
    num3 = num1 % num2
    print(f"Modulus: {num3}")

    # assignment operators
    # =, +=, -=, *=, /=, //=, **=, %=

    num1 = 10
    print(f"Initial value of num1: {num1}")
    num1 += 1
    print(f"After incrementing value by 1: {num1}")

    num1 = 5
    print(f"Initial value of num1: {num1}")
    num1 -= 1
    print(f"After decrementing value by 1: {num1}")

    num1 = 1
    print(f"Initial value of num1 is {num1}")
    num1 *= 10
    print(f"After multiplying value by 10: {num1}")

    num1 = 20
    print(f"Initial value of num1: {num1}")
    num1 /= 2
    print(f"After dividing value by 2: {num1}")

    num1 = 20
    print(f"Initial value of num1: {num1}")
    num1 //= 2
    print(f"After floor division by 2: {num1}")

    num1 = 2
    print(f"Initial value of num1 is : {num1}")
    num1 **= 2
    print(f"After exponenting by 2: {num1}")

    num1 = 50
    print(f"Initial value of num1 is : {num1}")
    num1 %= 5
    print(f"After modulus by 5: {num1}")

    # there will be a case, we always need +ve number
    # for that python provides built in function called abs()
    num1 = -20
    print(f"Absolute value of {num1} is {abs(num1)}")

    # in some cases we need to round off a value
    # for that python provides round() bulit in function
    num1 = 20.678
    print(f"{num1} rounded to next int value : {round(num1)}")

    # we can also round by desimal points
    print(f"{num1} rounded to 2 decimal points : {round(num1, 2)}")

    # comaprison operators in python
    print(1 == 1)
    print(1 < 2)
    print(1 <= 2)
    print(2 > 1)
    print(2 >= 1)

    # type casting in python
    num1 = "123"
    num2 = "321"
    print(f"Result without type casting: {num1 + num2}")
    print(f"Result with type casting: {int(num1) + int(num2)}")
