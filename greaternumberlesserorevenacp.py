number1 = int(input("PLeASE eNTER a number : "))  # Convert input to integer
number2 = int(input("Please enter another number : "))  # Convert input to integer

# Compare number1 with number2
if number1 < number2:
    print(number1, "is less than", number2)
elif number1 > number2:
    print(number1, "is greater than", number2)
else:
    print(number1, "is equal to", number2)

# Compare number2 with number1
if number2 < number1:
    print(number2, "is less than", number1)
elif number2 > number1:
    print(number2, "is greater than", number1)
else:
    print(number2, "is equal to", number1)