class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def info(self):
        print(f"this is a vehicle:{self.brand} {self.model}")
class Car(vehicle):
    def info(self):
        print(f"this is a vehicle:{self.brand} {self.model}")
    def number_of_doors(self):
        print("this car has 4 doors")
v = vehicle("GenericBrand", "ModelX")
v.info()

c = Car("Toyota", "Corolla")
c.info()
c.number_of_doors()          
          