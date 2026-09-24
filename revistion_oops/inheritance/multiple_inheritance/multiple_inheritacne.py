class Father:
    def __init__(self , name):
        self.name =name
        
    def show_father(self):
        print("father : "  , self.name)
        
class Mother:
    def __init__(self , Mother_name):
        self.Mother_name = Mother_name
        
    def show_Mother(self):
        print("Mother : "  , self.Mother_name)
        
class Child(Father , Mother):
    def __init__(self, name , Mother_name , Child_name):
        Father.__init__(self , name)
        Mother.__init__(self , Mother_name)
        self.Child_name = Child_name
        
    def show_child(self):
        print("Child : " , self.Child_name)
        
obj = Child("Ram " , "Sita" , "Rahul")
obj.show_father()
obj.show_Mother()
obj.show_child()                    
                 