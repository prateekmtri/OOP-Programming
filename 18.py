class laptop:
    def __init__(self , brand , battery):
        self.brand = brand
        self.__battery = battery
        
    def charge(self , amount):
        self.charge_battery = amount
        self.__battery = self.__battery+self.charge_battery
        print(f"Battery : {self.__battery}")
        
    def use(self , amount):
        self.use_battery = amount
        if self.__battery >= self.use_battery:
            self.__battery = self.__battery - self.use_battery
            print("Battery kam karo")
        else:
            print("Low battery")  
            
            
    def show_staus(self):
        print(f"Brand : {self.brand}")
        print(f"Battery : {self.__battery} ") 
        
        if self.__battery >= 50:
            print(f"Battery Good")
        else:
            print(f"Battery Low")
            
            
            
obj = laptop("Asus", 40)
obj.show_staus()
obj.charge(30)
obj.use(50)
obj.show_staus()                   
           
        
    
        