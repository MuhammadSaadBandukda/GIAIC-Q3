class Car:
    def __init__(self,brand):
        self.brand = brand
    
    def start(self):
        print(f"Car of brand {self.brand} is starting..." )


c1 = Car("toyota")
c1.start()