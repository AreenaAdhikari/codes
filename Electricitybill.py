units = int(input("please enter the amout of units you consumed: "))
if (units<50):
    amount = units * 2.60
    subcharge = 25
elif (units<=100):
    amount= 130 + ((units - 50)*3.25)
    subcharge = 35
elif (units<=200):
    amount= 130 + 162.50 ((units - 100)*5.26)
    subcharge = 45
else:

    amount= 130 + 162.50 + 523+ ((units - 100)*8.45)
    subcharge = 75
total = amount + subcharge
print("\n your electricity bill is = %.2f" %total)

 

