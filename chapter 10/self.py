class Employee:
    
    language = "python" #these are class attributes
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
        
    @staticmethod
    def greet():
        print("Good morning")


employee = Employee() # this is object of class Employee
employee.name = "Aakarshit" # this is an instance attributes
employee.language = "Java" 
employee.getInfo()
employee.greet()

