class Person(object):
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class Employee(Person):
    def __init__(self,name,idnumber,post,salary):
        self.post = post
        self.salary = salary
        Person.__init__(self,name,idnumber)
a = Employee('Rahul',881620,200200,"Intern")
a.display()