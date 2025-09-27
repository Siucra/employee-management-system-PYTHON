#subclass of Employee (child)
from Employee import Employee

class FullEmployee(Employee):

    #Constructor using super
    def __init__(self, employeeID,name,age,gender,status,rolefullHours,fullAmHour):
        
        #call parent class' constructor
        super().__init__(self, employeeID,name,age,gender,status)
        
        #child specific fields
        self.rolefullHours = rolefullHours
        self.fullAmHour = fullAmHour

        