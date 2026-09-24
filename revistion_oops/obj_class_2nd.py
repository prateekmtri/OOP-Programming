class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model
        
obj = Car("Toyota" , "Fortuner")
print("Brand : ",obj.brand)
print("Model: ",obj.model)        