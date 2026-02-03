class Salary:
    def __init__(self , overall_salary , in_hand_salary):
        self.overall_salary = overall_salary
        self.in_hand = in_hand_salary
        
        
    def show_overall(self):
        print(f"my overall salary {self.overall_salary}")
        
        
    def show_in_hand(self):
        print(f"i am founding {self.in_hand}")
        
        if self.in_hand > 40:
            print("and its high")
        else:
            print("and its too low")
            
obj = Salary(400 , 50)
obj.show_overall()
obj.show_in_hand()

                        
        