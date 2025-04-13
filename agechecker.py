def check_age():
    age_input = input("Enter your age : ")
    if not age_input.isdigit():
        print("Error : Age should be a positive number !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return
    age = int(age_input)







    if age <= 0 or age >130:
        print("Error : Please enter a valid age. age not realistic")
        return
    


    if age % 2 == 0 :
        print("your age ({age}) is even .")
    else:
        print("Your age is ({age}) is odd. ")
check_age()