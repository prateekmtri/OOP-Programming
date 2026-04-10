class Tv:
    def __init__(self , brand , volume):
        self.brand = brand
        self.__volume = volume
        
        
    def increse_volume(self , amount):
        self.__volume = self.__volume+amount
        print(f"New Volume : {self.__volume}")
        
    def decrese_volume(self , amount):
        if self.__volume >= amount:
                self.__volume = self.__volume - amount
                print(f"New Volume: {self.__volume}")
        else:
            print("volume is too low")
            
    def show_status(self):
        print(f"Brand : {self.brand}")
        print(f"Volume : {self.__volume}")
        
        if self.__volume >= 50:
            print("loud")
        else:
            print("Normal")  
            
            
obj = Tv("Sony", 30)
obj.show_status()
obj.increse_volume(40)
obj.decrese_volume(50)
obj.show_status()
                  