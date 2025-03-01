Amount= int(input("Please enter the amount u want to withdraw:"))
note_1= Amount//100
note_2= (Amount%100)//50
note_3= ((Amount%100)%50)//10

print("the 100 rupee notes is:" , note_1)
print("The 50 rupee notes is:" , note_2)
print("The 10 rupee notes is:" , note_3)