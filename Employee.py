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
        print(f"Employee ID:  {self.employeeID}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.gender}")
        print(f"Status: {self.status}")
        print("-"*16)

        if self.role is not None:
            #you can access attributes/methods directly on the object instead of self/'this'
            print(f"Job Title: {self.role.title}")
            print(f"Salary  {self.role.salary}")
        else:
            print("No role assigned.")
        
        if isinstance(self, FullEmployee):
            print(f"Part-time Hours: {self.fullHours}")				
            print(f"Hourly Rate: {self.fullAmHour}")

        elif isinstance(self, PartEmployee):
            print(f"Full-time Hours: {self.partHour}")
            print(f"Hourly Rate: {self.partAmHour}")
        
        print("-"*16)
        

    