from abc import ABC , abstractmethod

class HospitalPerson(ABC):
    def __init__(self , name , person_id):
        self.name = name
        self.__person_id = person_id
        
    def get_id(self):
        return self.__person_id
    
    @abstractmethod
    def work(self):
        pass
    
class Doctor(HospitalPerson):
    def work(self):
        print(self.name, " is treating patients") 
    
class Nurse(HospitalPerson):
    def work(self):
        print( self.name, "is taking care of patients") 
        
Obj_Doctor = Doctor("Prateek" , 6)
obj_Nurse = Nurse("Madhuri" , 9) 

print("Name : " , Obj_Doctor.name)
print("Id : " , Obj_Doctor.get_id())
Obj_Doctor.work()

print("Name : " , obj_Nurse.name)
print("Id : " , obj_Nurse.get_id())
obj_Nurse.work()
               