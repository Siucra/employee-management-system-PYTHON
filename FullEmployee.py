#subclass of Employee (child)
from Employee import Employee

class FullEmployee(Employee):

    #Constructor using super
    def __init__(self, employeeID,name,age,gender,status,role,fullHours,fullAmHour):
        
        #call parent class' constructor
        super().__init__(employeeID,name,age,gender,status,role)
        
        #child specific fields
        self.fullHours = fullHours
        self.fullAmHour = fullAmHour
    
    def __str__(self):
        #get base info from parent
        base = super().__str__().rstrip(")") #remove closing parenthesis
        return base + f", fullHours={self.fullHours}, fullAmHour={self.fullAmHour})"


        