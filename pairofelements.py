class pair_elements:
    def TwoSums(self,nums,target):
        lookup = {}

        for i,num in enumerate(nums):
            if target - num in lookup:
             return(lookup[target - num],i)
            lookup[num] = i
value = int(input("Enter a sum for which u want to make this sreach :"))
print("index1=%d,index2=%d" %
pair_elements().TwoSums((10,20,30,40,50,60,70),value))
