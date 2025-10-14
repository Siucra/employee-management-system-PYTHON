from Employee import Employee
from FullEmployee import FullEmployee
from PartEmployee import PartEmployee
from Role import Role


employee_list = []

def prepopulate(): #e = Employee("Alice", 50000)
    global employee_list

    r1 = Role("Maintenance",50000)
    fe1 = FullEmployee(1,"Bob",59,"Male","Senior",r1,40,18.05)
    
    r2 = Role("Janitor",300000)
    pe1 = PartEmployee(2,"Jen",21,"Female","Junior",r2,20,15.50)

    employee_list = [fe1,pe1]

def employeeMenu():
    print("*"*25)
    print("EMPLOYEE MANAGEMENT SYSTEM MENU")
    print("1 - Add Employee Menu")
    print("2 - Edit Employee Menu")
    print("3 - Fire Employee Menu")
    print("4 - View Employee Menu")
    print("*"*25)
    
    while True:
        choice = input("Enter a number (1-4): ")
        #python switch case(?)
        if choice =="1":
            print("Loading add employee....")
            addEmployeeMenu()
            break
        elif choice =="2":
            print("Loading edit employee....")
            #editEmployee()
            break
        elif choice =="3":
            print("Loading fire employee....")
            #fireEmployee
            break
        elif choice =="4":
            print("Loading view employee....")
            #viewEmployee
            break
        else:
            print("invalid input. Please try again")

def gen_id(start=1):
    while True:
        yield start
        start+=1

def addEmployeeMenu():
    print("-"*25)

    id_generator = gen_id(1)
    e = Employee(next(id_generator)) # ceeate new employee with next available ID

    print("")
    e.set_name(input())

    



def main():
    prepopulate()

if __name__ == "__main__": # calls main method
    main()






