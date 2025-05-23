class Student:
    def __init__(self,name:str,marks:int):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"{self.name} has {self.marks} marks")



def main():
    s = Student("Saad",14)
    s.display()


if __name__ == '__main__':
    main()