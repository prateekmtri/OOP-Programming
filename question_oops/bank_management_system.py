from abc import ABC , abstractmethod
class BankAccount(ABC):
    def __init__(self , name , balance , acount_number):
        self.name = name
        self.balance = balance
        self.__acount_number = acount_number
        
    def getter(self): 
        return self.__acount_number 
    
    def show_balance(self):
        print("Your balance is : " , self.balance)
    
    @abstractmethod
    
    def account_type(self):
        pass
    
class Saving_Account(BankAccount):
    def account_type(self):
        print(self.name , "have Savings Account")
      

class Current_Account(BankAccount):
    def account_type(self):
        print(self.name , "have Current Account")
        
        
        
obj1 = Saving_Account("Prateek", 101003, 6050)  
obj2 = Current_Account("vardayini", 103737, 6051)   

print("Name : " , obj1.name) 
print("balance : " , obj1.balance)
print("Account_number : " ,obj1.getter()) 
obj1.account_type() 

print("Name : " , obj2.name) 
print("balance : " , obj2.balance)
print("Account_number : " ,obj2.getter()) 
obj2.account_type() 
           
           