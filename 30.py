class Mobile:
    def __init__(self , brand , battery ):
        self.brand = brand
        self.__battery = battery
        
    def show_battery(self):
        print(f" Brand : {self.brand}")
        print(f"Battery : {self.__battery}")
        
            
        