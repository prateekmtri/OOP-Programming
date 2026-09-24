class Bankaccount:
    def __init__(self , account_holder , acount_type , balance):
        self.Accounnt_holder = account_holder
        self._Acount_type = acount_type
        self.__balance = balance
        
    def show_acount(self):
        print("Acount Holder : ", self.Accounnt_holder)
        print("Acount Type : ", self._Acount_type)
        print("Balance : " , self.__balance)
        return self.__balance
    
    def set_balance(self , balance):
        self.__balance = balance
        
obj = Bankaccount("Prateek " ,"Saving " , 25000)  
obj.show_acount()
print(obj.show_acount())# getter
obj.set_balance(10000)
print(obj.show_acount())
