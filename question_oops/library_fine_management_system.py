from abc import ABC , abstractmethod

class LibraryBorrowing(ABC):
    def __init__(self , member_name , member_id , day_late , fine_per_day):
        self.member_name = member_name
        self.__member_id = member_id
        self.day_late = day_late
        self.fine_per_day = fine_per_day
        
    def getter(self):
        return self.__member_id
    
    def setter(self , fine_per_day):
        self.fine_per_day = fine_per_day
        
    def show_fine_details(self):
        print(self.member_name)
        print(self.getter())
        print(self.day_late)
        print(self.fine_per_day)
        print(self.calculate_fine())
        
    @abstractmethod
    def calculate_fine(self):
        pass
    
class RegularMember(LibraryBorrowing):
    def calculate_fine(self):
        fine = self.day_late * self.fine_per_day
        return fine
    

class PremiumMember(LibraryBorrowing):
    def calculate_fine(self):
        fine = self.day_late * self.fine_per_day
        discount = fine * 20 / 100
        total = fine - discount
        return total
 
class SpecialMember(LibraryBorrowing):
    def calculate_fine(self):
        fine = self.day_late * self.fine_per_day
        if self.day_late > 7:
            fine = fine+ 200
            return fine
        else:
            return fine    


obj1 = RegularMember("Prateek", 101, 5, 20)
obj2 = PremiumMember("Rahul", 102, 10, 30)
obj3 = SpecialMember("Aman", 103, 8, 25)


obj1.setter(25)

obj1.show_fine_details()
print()
print() 
obj2.show_fine_details()
print()
print()  

obj3.show_fine_details()

    
                    