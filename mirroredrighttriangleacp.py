def mirrored_right_triangle(n):
    for i in range(1, n+1):
        print(" "*(n-i)+"*"*i)
n = int(input("Please enter the number of rows you want in the triangle : "))
mirrored_right_triangle(n)