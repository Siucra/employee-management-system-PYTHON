#subclass of Employee (child)
from Employee import Employee


class PartEmployee(Employee):

    #Constructor using super
    def __init__(self, employeeID,name,age,gender,status,partHour, partAmHour):
        
        #call parent class' constructor
        super().__init__(self, employeeID,name,age,gender,status)
        
        #child specific fields
        self.partHour = partHour
        self.partAmHour = partAmHour