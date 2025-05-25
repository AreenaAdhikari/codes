class IOSstring ():
    def __init__(self):
        self.str1 =""
    def get_String(self):
        self.str1 = input("Enter a string:")
    def print_string(self):
        print("Result is :",self.str1.upper())
str1 = IOSstring()
str1.get_String()
str1.print_string()
