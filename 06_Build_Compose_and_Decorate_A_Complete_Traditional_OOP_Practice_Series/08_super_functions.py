class Person:
    def __init__(self,name:str):
        self.name = name
    

class Teacher(Person):
    def __init__(self, name:str,subject:str):
        self.subject = subject
        super().__init__(name)


p = Person("Saad")
print(p.name)
t = Teacher("Ali Jawwad","Python")
print(t.name)
print(t.subject)