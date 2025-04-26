start =int(input("Enter a start of range :"))
end = int(input("Enter the end of the range : "))
square = [i**2 for i in range(start,end + 1)]
print("\nSquares of numbers from", start,"to", end, ":\n", square)
even_squares = [num for num in square if num % 2 == 0]
odd_squares = [num for num in square if num % 2 != 0]
print("\nEven squares values : ", even_squares)
print("Odd square values :", odd_squares)