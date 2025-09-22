


#subclass of Employee (child)
class PartEmployee:

    #Constructor using super
    def __init__(self, employeeID,name,age,gender,status,rolefullHours,fullAmHour):
        super.__init__(self, employeeID,name,age,gender,status)
        self.rolefullHours = rolefullHours
        self.fullAmHour = fullAmHour

        