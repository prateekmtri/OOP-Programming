class Employees:
    def __init__(self, name , salary , bonous):
        self.name = name
        self.salary = salary
        self.bonous = bonous
        
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary:{self.salary}")
        
        
    def check_bonous(self):
        print(f"Bonous:{self.bonous}")
        
        if self.bonous > 5000:
            print("Good bonus")
        else:
            print("low bonus")
            
    def total_income(self):
        print(f"overall salary is {self.salary+self.bonous}")        
            
obj = Employees("Prateek",40000 , 6000)
obj.show_details()
obj.check_bonous()
obj.total_income()
                
        