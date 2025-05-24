class Dog :
    species = "Canine"
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def show(self):
        print(f"{self.name} is a {self.breed} ({self.species})")
d1 = Dog("Tommy" , "labrador")
d2 = Dog("Bruno", "Beagle")
d1.show()
d2.show()