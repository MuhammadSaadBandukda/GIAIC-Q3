class Department:
    def __init__(self,name):
        self.name = name


class University:
    department = [] 
    def __init__(self,name:str):
        self.name = name

    def append_department(self,department:Department):
        self.department.append(department)
    

u = University("SMIU")
u.append_department("CS") 
u.append_department("SE") 
u.append_department("CY") 
u.append_department("BA") 
print(u.department)
