from FullEmployee import FullEmployee
from PartEmployee import PartEmployee

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
        print("-"*16)
        print("Employee ID: ", self.employeeID)
        print("Name: " +self.name)
        print("Age: "+ self.age)
        print("Sex: "+self.gender)
        print("Status: " + self.status)
        print("-"*16)

        if role is not None:
            #you can access attributes/methods directly on the object instead of self/'this'
            print("Job Title:", role.Title())
            print("Salary ",role.Salary())
        else:
            print("No role assigned.")
        
        if isinstance(self, FullEmployee):
            print("Part-time Hours: "+ self.PartHours())				
            print("Hourly Rate: " + self.PartAmHour())

        elif isinstance(self, PartEmployee):
            print("Full-time Hours: "+ self.FullHours())
            print("Hourly Rate: " + self.FullAmHour())
        
        print("-"*16)
        

    