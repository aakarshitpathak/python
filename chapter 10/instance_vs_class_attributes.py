class Employee:
    
    language = "python" #these are class attributes
    salary = 120000

employee = Employee() # this is object of class Employee
employee.name = "Aakarshit" # this is an instance attributes
employee.language = "Java" # note that instance attributes are preferred
# more than class attributes
print(employee.name , employee.language , employee.salary)

