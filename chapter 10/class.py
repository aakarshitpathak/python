class Employee:
    
    language = "python" #these are class attributes
    salary = 120000

employee = Employee() # this is object of class Employee
employee.name = "Aakarshit" # this is an instance attributes
print(employee.name , employee.language , employee.salary)

# Here name is object attributes and language and salary are class attributes
# because they are directly associated with class