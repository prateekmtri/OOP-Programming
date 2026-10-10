from abc import ABC , abstractmethod

class ATM(ABC):
    def __init__(self , customer_name , account_name , balance , amount):
        self.customer_name = customer_name
        self.__account_name = account_name
        self.balance = balance
        self.amount = amount
        
         
    def getter(self):
        return self.__account_name
    
    def setter(self , balance):
        self.balance = balance
        
    def show_transiction_details(self):
        print(self.customer_name)
        print(self.getter())
        print(self.amount)
        print(self.process_transiction())
    @abstractmethod    
    def process_transiction(self):
        pass
    
class Deposite(ATM):
    def process_transiction(self):
        final_balance = self.balance + self.amount
        return final_balance

class Withdrawal(ATM):
    def process_transiction(self):
        final_balance = self.balance - self.amount
        return final_balance
    
class BankTransfer(ATM):
    def process_transiction(self):
        final_balance = self.balance - self.amount - 50
        return final_balance   
    
    
    
obj1 = Deposite("Prateek", 101, 5000, 1000)
obj2 = Withdrawal("Rahul", 102, 8000, 2000)
obj3 = BankTransfer("Aman", 103, 10000, 3000)  


obj1.setter(6000)  

obj1.show_transiction_details()
print()
print()
obj2.show_transiction_details()
print()
print()
obj3.show_transiction_details() 
                                        
                                        
                                        