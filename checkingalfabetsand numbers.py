char = input("Enter a character or number: ")
if char.isalpha():
    print(f"{char} is an alphabet")
else:
    print(f"{char} is not an alphabet; it's a number")