class BankAccount:
    def __init__(self , name , balance , deposite , withdrwal):
        self.name = name
        self.balance = balance
        self.deposite = deposite
        self.withdraw = withdrwal
        
    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Balance: {self.balance}")    
        
    def show_deposite(self):
        print(f"deposite : {self.deposite}")
        print(f"New Balance : {self.balance + self.deposite}")
        
        if self.balance > 10000:
            print("healthy account")
        else:
            print("Account is not healthy")    
        
    def  show_withdrwal(self):
        print(f"Withdrawl : {self.withdraw}")
        
        if self.withdraw > self.balance:
            print("Insufficient ")
            

obj = BankAccount("Prateek" ,150000 , 5000 , 200000 )
obj.show_details()
obj.show_deposite()
obj.show_withdrwal()
