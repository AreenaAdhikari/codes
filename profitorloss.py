cost_amount = float(input(" Please enter how much you bought the product for: "))
sale_amout = float(input(" Please enter sales amount: "))
if (sale_amout > cost_amount):
  amount= sale_amout - cost_amount
  print("This is a profit = {0}".format (amount))
else:
 print("No Profit!!!")