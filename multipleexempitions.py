try:
 num1, num2 = eval(input("Enter a number , seperated by a comma :"))
 result = num1 / num1
 print("The result is ", result)
except ZeroDivisionError:
      print("division by zero is error")
except SyntaxError:
   print("THER IS NO COMMA , comma is missing")
except:
   print("Wrong input")
else:
   print("There is no execptions")
finally:
   print("This will execute no matter what ")