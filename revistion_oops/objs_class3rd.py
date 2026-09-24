class Mobile:
    def __init__(self, componey , price):
        self.componey = componey
        self.price = price
        
obj1 = Mobile("Sumsung" , 25000)
obj2 = Mobile("Realme" , 30000)

print("Componey : " , obj1.componey) 
print("Price : " , obj1.price)   
print("Componey : " , obj2.componey) 
print("Price : " , obj2.price)    