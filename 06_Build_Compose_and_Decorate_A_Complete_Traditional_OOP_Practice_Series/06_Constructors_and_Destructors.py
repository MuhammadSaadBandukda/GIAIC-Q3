class Logger:
    def __init__(self):
        print("Object is created")
    
    def __del__(self):
        print("Object is destroyed")


l = Logger()
del l
