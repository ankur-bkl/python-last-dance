class Car:
    
    color="black"
    @staticmethod
    def start():
        print("Car Started....")
        
    @staticmethod
    def stop():
        print("Car Stopped....")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        
car1=ToyotaCar("Fortuner")

car2=ToyotaCar("Pirus")

print(car1.start()) #it will print None as there is no return statement 

car1.start() 
car2.stop()

print(car2.name)