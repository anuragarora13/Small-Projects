class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def start(self):
        return  f"{self.brand}  {self.model} is starting"


class Car(Vehicle):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type = fuel_type
    def start(self):
        return f"{self.brand}  {self.model} {self.fuel_type} is starting Silently"
    # def drive(self):
    #     return f"Driving a {self.fuel_type} car!!"



car=Car("Tesla","Model S","electric")
print(car.start())
# print(car.drive())