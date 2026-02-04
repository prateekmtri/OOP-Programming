class Result:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
        
    def show_result(self):
        print(f"My Name is {self.name} and i got {self.marks}")
        
        if self.marks >= 80:
            print("Grade A")
        elif self.marks >= 50:
            print("Grade B")
        else:
            print("Grade C") 
        
object = Result("Prateek", 100)
object.show_result()
