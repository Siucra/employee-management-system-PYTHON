from Role import Role;

#Parent class
class Employee:

    #Constructor with Fields
    def __init__(self, id=None,name="",age=0,gender="",status="",role=None):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.status = status
        self.role = role

    #Print Employee Details
    def viewEmployeeDetails(self):
        print(self) # aka print(str(self)) -> uses __str__()
        
        
    def __str__(self):
        base = (
            f"Employee "
            f"ID = {self.id}\n"
            f"Name = {self.name}\n"
            f"Age = {self.age}\n"
            f"Gender = {self.gender}\n"
            f"Status = {self.status}\n"
        )

        if self.role is not None:
            base += f"Role = {self.role}\n"

        base += ")"
        return base

    