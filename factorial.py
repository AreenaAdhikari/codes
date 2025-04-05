def factorial(x):
    '''This is a recursive fuction to find the factorial of an intiger'''

    if x==0 or x==1 :
             return 1
    else:
        return x*factorial(x-1)

print(factorial.__doc__)
print("The factorial of 0 ", factorial(0))
print("The factorial of 1 ", factorial(1))
print("The factorial of 4 ", factorial(4))
print("The factorial of 5", factorial(10))
print("The factorial of 10 ", factorial(10))

