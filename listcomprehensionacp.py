words = ['apple','cherry','banana']
uppercased = [word.upper() for word in words]
print(uppercased)
nums = [1,2,7,10,13,16]
odd = [x for x in nums if x%2 == 1]
print(odd)
scores = [10,20,30,40]
added = [x + 5 for x in scores]
print(added)