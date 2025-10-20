#subclass of Employee (child)
from Employee import Employee

class PartEmployee(Employee):

    #Constructor using super
    def __init__(self, employeeID,name,age,gender,status,role,partHour, partAmHour):
        
        #call parent class' constructor
        super().__init__(employeeID,name,age,gender,status,role)
        
        #child specific fields
        self.partHour = partHour
        self.partAmHour = partAmHour
    
    def __str__(self):
        #get base info from parent
        base = super().__str__().rstrip(")") # remove closing parenthesis
        return base + f", partHour={self.partHour},partAmHour={self.partAmHour})"