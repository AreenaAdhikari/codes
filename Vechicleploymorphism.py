
class Car:
    def start_engine(self):
        pass
    def drive(self):
        pass
class BMW(Car):
    def start_engine(self):
        print("BMW ENGINE STARTED WITH A ROAR !")
    def drive(self):
        print("BMW is driving smoothly on the highway. ")
def test_drive(car):
    car.start_engine()
    car.drive()
bmw_car = BMW()
test_drive(bmw_car)
print()