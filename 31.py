class Fan:
    def __init__(self , brand):
        self.brand = brand
        self.__is_on = False
        self.__speed = 0    
            
            
    def turn_on(self):
        if self.__is_on == False:
            self.__is_on = True
            print(f"Fan is on ")
        else:
            print("fan is alredy on")    
            
    def turn_off(self):
        if self.__is_on==True:
            self.__is_on=False
            print(f"fan is off")
        else:
            print("fan is alredy off")
                
    def increase_speed(self, amount):
        if self.__is_on:
            self.__speed += amount
            if self.__speed > 5:
                self.__speed = 5
                print("Maximum speed reached")
            else:
                print(f"Speed increased to {self.__speed}")
        else:
            print("Fan is OFF")
            
    def decrese_speed(self , amount):
        if self.__is_on:
            self.__speed -= amount
            if self.__speed < 0:
                self.__speed = 0
                print("Minimum speed reached")
            else:
                print(f"Speed decrese to {self.__speed}")
        else:
            print("Fan is off")            
    
    def show_status(self):
        print(f"Brand : {self.brand}")
        print(f"Status : {self.__is_on}")
        print(f"Current Speed : {self.__speed}" )                        
            
                    
obj = Fan("Usha")
obj.turn_on()
obj.increase_speed(3)
obj.show_status()
obj.decrese_speed(1)
obj.show_status()                    