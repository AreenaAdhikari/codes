def multiply_tuple_element(numbers):
  product = 1
  for num in numbers:
    product+=num
    return product
my_tuple = (2,3,5,7)
result = multiply_tuple_element(my_tuple)
print("The product of all the tuple elements is : " , result)