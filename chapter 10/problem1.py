class Programmer:
    company = "Microsoft"
    def __init__(self , name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Aakarshit", 2400000, 226017)
print(p.name, p.salary , p.pin , p.company)

r = Programmer("Rahul", 2400000, 226017)
print(r.name, r.salary , r.pin , r.company)

