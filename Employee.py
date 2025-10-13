from Role import Role;

#Parent class
class Employee:

    #Constructor with Fields
    def __init__(self, employeeID,name,age,gender,status,role):
        self.employeeID = employeeID
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
        f"employeeID={self.employeeID}, "
        f"name={self.name}, "
        f"age={self.age}, "
        f"gender={self.gender}, "
        f"status={self.status}"
    )

    if self.role is not None:
        base += f", role={self.role}"

    base += ")"
    return base

    