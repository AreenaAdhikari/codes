try:
 number = int(input("Enter a Number : "))
 print("THE NUMBER IS :" ,number)
except ValueError  as ex :
  print("Exception : " ,ex)
