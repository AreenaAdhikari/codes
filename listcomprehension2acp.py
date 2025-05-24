words = ['car1','car2','car3']
uppercased = [word.upper() for word in words]
print(uppercased)
nums =[1,2,34,76,5,7,89,98,0,3,]
odds = [x for x in nums if x %2 == 1]
print(odds)
scores = [10,20,30,40,50,60,7000,700,12345,1234]
added = [x + 5 for x in scores]
print(added)