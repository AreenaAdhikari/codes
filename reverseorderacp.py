num = int(input("Enter a number :) :"))
count = 0
temp = abs(num)
while temp > 0:
   temp //= 10
   count += 1
if num == 0:
   count = 1

print("Total digits in the number ", count)
