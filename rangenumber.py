lower = int(input("Please enter a lower range number: "))
Upper = int(input("Please enetr a Upper range number : "))
print("The range between ", lower, "and",Upper, "are:")
for num in range(lower,Upper+1):
    if num > 1:
     is_prime = True
     for i in range(2,int(num**0.5)+1):
       if num % i == 0:
        is_prime= False
        break
       if is_prime:
        print(num)