medical_cause = input("did you have a medical cause Y or N : ")
atten = int(input("enter the students attendance : "))
if medical_cause=='Y':
    print("You are allowes to")
else:
 if atten>=75:
    print("you are allowed to")
 else:
   print("you are not allowed to")

