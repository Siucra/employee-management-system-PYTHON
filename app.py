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
            editEmployee()
            break
        elif choice =="3":
            print("Loading fire employee....")
            #fireEmployee
            break
        elif choice =="4":
            print("Loading view employee....")
            for emp in employee_list:
                emp.viewEmployeeDetails()
                print("-"*20)
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

    e.name = input("Enter Employee name: ")

    while True:
        ageInput = input("Enter Employee age: ")
        if ageInput.isdigit(): #error catching without using try/except -> checks if user entered only integers
            e.age = int(ageInput)
            if e.age > 0:
                break
            else:
                print("Age must be greater than zero.")
        else:
            print("Invalid input. Please enter a number.")

    while(True):
        e.gender = input("Enter Employee gender: ")
        if e.gender.lower()=="male" or e.gender.lower()=="female":
            break
        else:
            print("Invalid input. Please either enter 'Male' or 'Female")
    
    while(True):
        e.status = input("Enter Employee status: Junior/Senior ")
        if e.status.lower() =="junior" or e.status.lower()=="senior":
            break
        else:
            print("invalid input. Please enter 'Junior' or 'Senior'")

    title = input("Enter Employee Job Title: ")
    salary = float(input("Enter employee annual salary: "))

    r = Role(title,salary)

    while(True):
        print("-"*15)
        empType = input("Is this Employee Part/Full? Enter  ('Part' or 'Full') ")
        
        if empType.lower() == 'part':
            print("'Part' option has been selected")
           # PartEmployee(e,r)
            addPartEmployee(e,r)
            break
        
        elif empType.lower() == 'full':
            print("'Full' option has been selected")
            addFullEmployee(e,r)
            break
        
        else:
            print("Invalid input. Please try again.")
            

def addPartEmployee(e,r):
    partHour = int(input("Add part time hours: (15-30) "))
    partAmHour = float(input("Enter amount per hour: "))

    print(f"\n--- Preview of New Part-Time Employee---")
    print(f"ID: {e.id}")
    print(f"Name: {e.name}")
    print(f"Age: {e.age}")
    print(f"Gender: {e.gender}")
    print(f"Status: {e.status}")
    print(f"Role Title: {r.title}")
    print(f"Role Salart: {r.salary}")
    print(f"Full-time hours: {partHour}")
    print(f"Amount per hour: {partAmHour}")

    while True:
        choice = input("Are you sure you want to create a Part time employee (YES/NO): ")
        
        if choice =="yes".strip().lower():
            pe = PartEmployee.from_employee(e,r)
            pe.partHour = partHour
            pe.partAmHour = partAmHour
            employee_list.append(pe)
            print(f"Employee {pe.name} has been added.")
            break

        elif choice == "no".strip().lower():
            print(f"Discarded employee record {pe.name}.")
            break
        else:
            print(f"Invalid entry, discarded employee record {e.name}.")
            break


def addFullEmployee(e,r):
    fullHours = int(input("Add full time hours: (30-40) "))
    fullAmHour = float(input("Enter amount per hour: "))

    print(f"\n--- Preview of New Full-Time Employee---")
    print(f"ID: {e.id}")
    print(f"Name: {e.name}")
    print(f"Age: {e.age}")
    print(f"Gender: {e.gender}")
    print(f"Status: {e.status}")
    print(f"Role Title: {r.title}")
    print(f"Role Salart: {r.salary}")
    print(f"Full-time hours: {fullHours}")
    print(f"Amount per hour: {fullAmHour}")

    while True:
        choice = input("Are you sure you want to create a Full time employee (YES/NO): ")
        
        if choice =="yes".strip().lower():
            fe = PartEmployee.from_employee(e,r)
            fe.fullHours = fullHours
            fe.fullAmHour = fullAmHour
            employee_list.append(fe)
            print(f"Employee {fe.name} has been added.")
            break

        elif choice == "no".strip().lower():
            print(f"Discarded employee record {fe.name}.")
            break
        else:
            print(f"Invalid entry, discarded employee record {e.name}.")
            break

def editEmployee():
    for emp in employee_list:
        emp.viewEmployeeDetails()
        print("-"*20)
        break

    user_input = input("Enter Employee ID you wish to edit")
    if not user_input.isdigit():
        print("Invalid ID. Please try again.")
        return
    
    searchID = int(user_input)
    id_is_found = False
    

def main():
    prepopulate()
    employeeMenu()

if __name__ == "__main__": # calls main method
    main()






