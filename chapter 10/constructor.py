class Employee:
    
    language = "python" #these are class attributes
    salary = 120000

    def __init__(self): # dunder method which is automatically called
        print("I am creating an object") 

        
    @staticmethod
    def greet():
        print("Good morning")


employee = Employee() # this is object of class Employee
employee.name = "Aakarshit"
print(employee.name, employee.salary)

rohan = Employee()  # jitne baar hum object banayenge utne baar 
                    # automatically init call hojayega 