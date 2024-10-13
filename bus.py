class Vehicle:

    def __init__(self,name,max_speed,mileage,capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    
    def fare(self):
        return self.capacity * 100
    
class Bus(Vehicle):

    def fare(self):
        amount = super().fare()
        amount = amount + ( amount * 10/100)
        return amount
School_bus = Bus("School Volvo ", 180, 12, 50)

print("Vehicle Name: ", School_bus.name, "\nSpeed: ", School_bus.max_speed , "\nMileage: ", School_bus.mileage)

print("Total bus fare: ", School_bus.fare())