from abc import ABC , abstractmethod

class LibraryMember(ABC):
    def __init__(self , name , member_id , book_issued):
        self.name = name
        self.__member_id = member_id
        self.book_issued = book_issued
        
    def getter(self):
        return self.__member_id
    
    def setter(self , book_issued):
        self.book_issued = book_issued
        
    def show_details(self):
        print(self.name)
        print(self.getter())
        print(self.book_issued)
        print(self.calculate_fine())    
    
    
    @abstractmethod
    def calculate_fine(self):
        pass
    
    
    
class Regular_member(LibraryMember):
    def calculate_fine(self):
        R_fine = self.book_issued*10
        return R_fine
    
class PremiumMember(LibraryMember):
    def calculate_fine(self):
        P_fine = self.book_issued*5
        return P_fine   
    
    
obj1 = Regular_member("Prateek", 101, 3)
obj2 = PremiumMember("Rahul", 102, 4)

obj1.setter(5)

obj1.show_details()
print()
print()
obj2.show_details()     
    
    
                
        