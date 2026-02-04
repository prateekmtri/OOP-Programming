class BankAccount:
    def __init__(self , name , balance):
        self.name = name
        self.__balance = balance
            
        
    def show_deposite(self , ammount):
        self.deposite_ammount = ammount
        self.__balance = self.__balance+self.deposite_ammount
        print(f"Deposite : {self.deposite_ammount}")
        print(f"New balance : {self.__balance}")
            
        
    def  show_withdrwal(self , ammount):
        self.withdrawl = ammount
       
        
        if self.withdrawl <= self.__balance:
             self.__balance = self.__balance - self.withdrawl
             print(f"withdrwal: {self.withdrawl}")
             print(f"Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance")
            
                
            
    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Balance: {self.__balance}")
        
        if self.__balance >=10000:
            print("Account is healthy")
        else:
            print("Low Balance")
            
            
    def get_balance(self):
        print(f"Balance : {self.__balance}")                    
            

obj = BankAccount("Prateek" ,150000 )
obj.show_details()
obj.show_deposite(15000)
obj.show_withdrwal(5000)
obj.get_balance()



obj.__balance = -999999
obj.show_details()
