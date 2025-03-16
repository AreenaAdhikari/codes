num = int(input("please Enter a number : "))
temp = num
am=0
while temp >0:
    digit = temp % 10
    am += digit ** 3
    temp //= 10

if num == am:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
