class Car:
    def __init__(self , brand , fuel):
        self.brand = brand
        self.__fuel = fuel
        
    def refule(self , amount):
        self.__fuel = self.__fuel+amount
        print(f"New fuel : {self.__fuel}")
        
    def drive(self , km):
        if self.__fuel >= km:
            self.__fuel = self.__fuel - km
            print(f"Remaning fuel : {self.__fuel}")
        else:
            print("Not enough fuel")
            
    def show_status(self):
        print(f"Brand :{self.brand} ")
        print(f"Fuel: {self.__fuel}")
        
        if self.__fuel >= 50:
            print("Ready for a long drive")
        else:
            print("Need fuel")
            
            
            
obj = Car("Tata", 40)
obj.show_status()
obj.refule(30)
obj.drive(50)
obj.show_status()
                              