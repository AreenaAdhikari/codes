class myClass:
    __privateVar = 27
    def __privateMeth(self):
        print("I'M inside class myClass")
    def __hello(self):
        print("Private varible value :",myClass.__privateVar)
foo = myClass()
foo.hello()
foo.__privteMeth()