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
        # Lazy import to avoid circular import
        from FullEmployee import FullEmployee
        from PartEmployee import PartEmployee

        print("-"*16)
        print("Employee ID: ", self.employeeID)
        print("Name: " +self.name)
        print("Age: "+ self.age)
        print("Sex: "+self.gender)
        print("Status: " + self.status)
        print("-"*16)

        if self.role is not None:
            #you can access attributes/methods directly on the object instead of self/'this'
            print("Job Title:", self.role.title)
            print("Salary ", self.role.salary)
        else:
            print("No role assigned.")
        
        if isinstance(self, FullEmployee):
            print("Part-time Hours: "+ self.fullHours)				
            print("Hourly Rate: " + self.fullAmHour)

        elif isinstance(self, PartEmployee):
            print("Full-time Hours: "+ self.partHour)
            print("Hourly Rate: " + self.partAmHour)
        
        print("-"*16)
        

    