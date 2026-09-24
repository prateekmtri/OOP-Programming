class Bank_account:
    def __init__(self , balance):
        self.__balance = balance
    
    def show_balance(self):
        print(self.__balance)  
        
obj = Bank_account(10000)
obj.show_balance()         