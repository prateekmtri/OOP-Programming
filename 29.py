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
        
        
class Patient:
    def __init__(self , patient_id , name ):
        self.patient_id = patient_id
        self.name =  name
        self.doctor_assigned = []
        
    def show_patient_info(self):
        print(f"Patient id : {self.patient_id}")
        print(f"Patient Name : {self.name}")
        print(f"Doctor Assigned to patience : {self.doctor_assigned}")
        
        
class Hospital:
    def __init__(self):
        self.doctor = []
        self.patience = []
        
    def add_doctor(self , doctor_object):
        self.doctor.append(doctor_object)
    
    def add_patient(self, patient_object):
        self.patience.append(patient_object)                  
    
    def assign_doctor(self , doctor_id , patient_id):
        for d in self.doctor:
            if d.doctor_id == doctor_id:
                for p in self.patience:
                    if p.patient_id == patient_id:
                        d.assign_patient()
                        p.doctor_assigned.append(d.name)            
                                    