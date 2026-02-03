class City:
    def __init__(self, city):
        self.city = city
        
    def show_city(self):
        print(f"I live in {self.city}")
        
obj = City("Gorakhpur")
obj.show_city()
             
        