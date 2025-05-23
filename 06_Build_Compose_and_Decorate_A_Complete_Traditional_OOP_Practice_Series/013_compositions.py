class Engine:
    def __init__(self):
        print("Hello from Engine")

    def start(self):
        print("Engine is starting...")

class Car:
    def __init__(self):
        self.engine= Engine()

    def start(self):
        print("Switch is on")
        self.engine.start()
        print("Car has started")



c = Car()
c.start()