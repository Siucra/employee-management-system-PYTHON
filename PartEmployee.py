#subclass of Employee (child)
class PartEmployee:

    #Constructor using super
    def __init__(self, employeeID,name,age,gender,status,partHour, partAmHour):
        super.__init__(self, employeeID,name,age,gender,status)
        self.partHour = partHour
        self.partAmHour = partAmHour