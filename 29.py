class Doctor:
    def __init__(self, doctor_id , name , specilization):
        self.doctor_id = doctor_id
        self.name = name
        self.specilization = specilization
        self.__is_available = True
        
    def show_doctor(self):
        print(f"Doctor Id : {self.doctor_id}")
        print(f"Doctor Name : {self.name}")
        print(f"Specilization : {self.specilization}")
        print(f"Doctor availability : {self.__is_available}")
        
    def assign_patient(self):
        if self.__is_available == True:
            self.__is_available = False
            print(" Patient is assign")
        else:
            print("Doctor not available")
            
    def complete_checkup(self):
        if self.__is_available ==False:
            self.__is_available = True
            print("checkup is complete")
        else:
            print("Busy")                      