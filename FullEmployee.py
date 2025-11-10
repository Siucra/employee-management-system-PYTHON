#subclass of Employee (child)
from Employee import Employee

class FullEmployee(Employee):

    #Constructor using super
    def __init__(self, id=None,name="",age=0,gender="",status="",role=None,fullHours=0,fullAmHour=0.0):
        
        #call parent class' constructor
        super().__init__(id,name,age,gender,status,role)
        
        #child specific fields
        self.fullHours = fullHours
        self.fullAmHour = fullAmHour
    
    def __str__(self):
        #get base info from parent
        base = super().__str__().rstrip(")") #remove closing parenthesis
        return base + f"Full-time hours = {self.fullHours}\nAmount per hour ={self.fullAmHour}"

@classmethod
def from_employee(cls,emp,role):
    return cls(emp.id,emp.name,emp.age,emp.gender,emp.status,role)   
        