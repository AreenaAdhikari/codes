print("Half Pyramid of Stars (*):")
n = int(input("Please enter the number of rows you wants : "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()