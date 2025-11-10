#subclass of Employee (child)
from Employee import Employee

class PartEmployee(Employee):

    #Constructor using super
    def __init__(self, id=None, name="", age=0, gender="", status="", role=None,partHour =0, partAmHour =0.0):
        
        #call parent class' constructor
        super().__init__(id,name,age,gender,status,role)
        
        #child specific fields
        self.partHour = partHour
        self.partAmHour = partAmHour
    
    def __str__(self):
        #get base info from parent
        base = super().__str__().rstrip(")") # remove closing parenthesis
        return base + f"Part-time hours = {self.partHour}\nAmount per hour = {self.partAmHour}"
    
#belongs to the class - recieves class (cls) - no need to manually unpack every field when converting Employee to partEmployee    
@classmethod
def from_employee(cls,emp,role):
    return cls(emp.id,emp.name,emp.age,emp.gender,emp.status,role)    