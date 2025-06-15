class Integerroman:
    def __init__(self,number):
        self.number = number
    def convert(self):
        val = [
            1000,900,500,400,
            100,90,50,40,
            10,9,5,4,
            1
        ]
        sysm = [
            "M","CM","D","CD",
            "C","XC","L","XI",
            "X","IX","V","IV",
            "I"
        ]
        roman_num = ""
        num = self.number
        for i in range(len(val)):
            while num >= val[i]:
                roman_num += sysm[i]
                num -= val[i]
        return roman_num
        
number = int(input("Enter an integer (1-3999): "))
converter = Integerroman(number)
print("Roman numeral: ", converter.convert())