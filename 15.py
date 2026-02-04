class BankAccount:
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance
            
        
    def show_deposite(self , ammount):
        self.deposite_ammount = ammount
        self.balance = self.balance+self.deposite_ammount
        print(f"Deposite : {self.deposite_ammount}")
        print(f"New balance : {self.balance}")
            
        
    def  show_withdrwal(self , ammount):
        self.withdrawl = ammount
       
        
        if self.withdrawl <= self.balance:
             self.balance = self.balance - self.withdrawl
             print(f"withdrwal: {self.withdrawl}")
             print(f"Remaining Balance: {self.balance}")
        else:
            print("Insufficient balance")
            
                
            
    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Balance: {self.balance}")
        
        if self.balance >=10000:
            print("Account is healthy")
        else:
            print("Low Balance")            
            

obj = BankAccount("Prateek" ,150000 )
obj.show_details()
obj.show_deposite(15000)
obj.show_withdrwal(5000)
