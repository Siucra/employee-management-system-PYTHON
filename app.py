from Employee import Employee
from FullEmployee import FullEmployee
from PartEmployee import PartEmployee
from Role import Role


employee_list = []

def main():
    prepopulate()

if __name__ == "__main__": # calls main method
    main()

def prepopulate(): #e = Employee("Alice", 50000)
    r1 = Role("Maintenance",50000)
    fe1 = FullEmployee(1,"Bob",59,"Male","Senior",r1,40,18.05)
    
    r2 = Role("Janitor",300000)
    pe1 = PartEmployee(2,"Jen",21,"Female","Junior",r2,20,15.50)

    employee_list = [r1,r2]