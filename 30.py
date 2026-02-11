class Mobile:
    def __init__(self , brand  ):
        self.brand = brand
        self.__battery = 20
        
    def show_battery(self):
        print(f" Brand : {self.brand}")
        print(f"Battery : {self.__battery}")
        
    def charge(self , ammount):
            self.__battery = self.__battery + ammount
            print(f"New Battery : {self.__battery}")
                    

class Charger:
    def charge_mobile(self , mobile_object , amount):
        mobile_object.charge(amount)
        
        
        
m = Mobile("vivo")
c = Charger()

m.show_battery()
c.charge_mobile(m, 30)
m.show_battery()
   
                