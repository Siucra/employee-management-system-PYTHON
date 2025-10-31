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
            f"id = {self.id}\n "
            f"name = {self.name}\n "
            f"age = {self.age}\n "
            f"gender = {self.gender}\n "
            f"status = {self.status}\n"
        )

        if self.role is not None:
            base += f"role = {self.role}\n"

        base += ")"
        return base

    