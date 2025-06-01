class Vehicle:
    def __init__(self,name,max_speed,mileage,faire):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.faire = faire
class Bus(Vehicle):
    pass
School_bus = Bus("School Volvo",180,12,20-30)
print("Vehicle name: ",School_bus.name,"Speed :",School_bus.max_speed,"Mileage:",School_bus.mileage,"Bus faire :",School_bus.faire)