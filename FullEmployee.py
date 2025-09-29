#subclass of Employee (child)
from Employee import Employee

class FullEmployee(Employee):

    #Constructor using super
    def __init__(self, employeeID,name,age,gender,status,fullHours,fullAmHour):
        
        #call parent class' constructor
        super().__init__(employeeID,name,age,gender,status)
        
        #child specific fields
        self.fullHours = fullHours
        self.fullAmHour = fullAmHour

        