from abc import ABC , abstractmethod

class BankAccount(ABC):
    def __init__(self , account_holder , account_number , balance):
        self.account_holder = account_holder
        self.__account_number = account_number
        self.balance = balance
        
    def geter(self):
        return self.__account_number
    
    def setter(self , balance):
        self.balance = balance
        
    def show_details(self):
        print(self.account_holder)
        print(self.geter())
        print(self.balance)
        print(self.calculate_intrest())     
        
    @abstractmethod
    def calculate_intrest(self):
        pass
    
class Saving_account(BankAccount):
    def calculate_intrest(self):
        intrest = self.balance*5/100
        return intrest 
    
class CurrentAccount(BankAccount):
    def calculate_intrest(self):
        intrest = self.balance*2/100
        return intrest    
    
    
obj1 = Saving_account("Prateek", 101, 50000)
obj2 = CurrentAccount("Rahul", 102, 80000)

obj1.setter(60000)

obj1.show_details()
print()
print()
obj2.show_details()        
    
    
           