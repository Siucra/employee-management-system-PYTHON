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
        f"Employee("
        f"id={self.id}, "
        f"name={self.name}, "
        f"age={self.age}, "
        f"gender={self.gender}, "
        f"status={self.status}"
    )

    if self.role is not None:
        base += f", role={self.role}"

    base += ")"
    return base

    