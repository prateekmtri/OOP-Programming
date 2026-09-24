class Shop:
    def __init__(self , price):
        self.Price = price
        
    def get_price(self):
        return self.Price
    
    def set_Price(self , price):
        self.Price = price
        

account = Shop(500)
print(account.get_price())
account.set_Price(750)
print(account.get_price())            