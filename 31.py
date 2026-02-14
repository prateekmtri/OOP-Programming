class Fan:
    def __init__(self , brand):
        self.brand = brand
        self.__is_on = False
        
    def show_status(self):
        if self.__is_on == False:
            print("Fan is off")
            
            
    def turn_on(self):
        if self.__is_on == False:
            self.__is_on = True
            print(f"Fan is : {self.__is_on}")
            
    def turn_off(self):
        if self.__is_on==True:
            self.__is_on=False
            print(f"Fan is : {self.__is_on}")
                
                    