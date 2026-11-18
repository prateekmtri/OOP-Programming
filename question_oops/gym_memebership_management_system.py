from abc import ABC , abstractmethod

class GymMembership(ABC):
    def __init__(self , member_name , member_id , monthly_fee , months_endrolled ):
        self.member_name = member_name
        self.__member_id = member_id
        self.monthly_fee = monthly_fee
        self.months_endrolled = months_endrolled
        
    def getter(self):
        return self.__member_id
    
    def setter(self ,months_endrolled):
        self.months_endrolled = months_endrolled
        
    def show_membership_details(self):
        print(self.member_name)
        print(self.getter())
        print(self.monthly_fee)
        print(self.months_endrolled)
        print(self.calculate_fee())
        
    @abstractmethod   
    def calculate_fee(self):
        pass
    

class BasicMember(GymMembership):
    def calculate_fee(self):
        total =  self.monthly_fee* self.months_endrolled
        return total
    
class PremiumMember(GymMembership):
    def calculate_fee(self):
        total =  self.monthly_fee* self.months_endrolled
        if self.months_endrolled >= 6:
            discount = total* 15/100
            return total - discount
        else:
            return total
        
class CorporateMember(GymMembership):
    def calculate_fee(self):
        total =  self.monthly_fee* self.months_endrolled
        discount = total* 20/100
        return total - discount

obj1 = BasicMember("Shivam", 301, 1000, 3)
obj2 = PremiumMember("Prateek", 302, 1500, 6)
obj3 = CorporateMember("Manish", 303, 1200, 12)

obj1.setter(4)

obj1.show_membership_details()
print()
obj2.show_membership_details()
print()
obj3.show_membership_details()    