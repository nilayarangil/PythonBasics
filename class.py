class Car:
    def __init__(self,brand):
        self.brand = brand
    def Getspeed(self):
        print(self.brand,"is very fast")

car1 = Car("BMW")
print("u have a",car1.brand)
car1.Getspeed()