class Sub:
    "How many subject i have in this year"
    def __init__(self , subject):
        self.subject = subject
        
    def show_subject(self):
        for sub in self.subject:
            print(sub)    
        
object = Sub(["Physics","Chemistry","Math","Hindi", "English"])
object.show_subject()