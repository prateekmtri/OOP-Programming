class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        
    def result(self):
        print(f"Name : {self.name}")
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")
            
            
obj = Student("Prateek" , 60)
obj.result()                   
                    
        