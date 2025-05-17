class Hospital:
    def __init__(self, name, location):
        self.hospital_name = name
        self.hospital_location = location
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def remove_doctor(self, doctor_name):
        self.doctors = [doc for doc in self.doctors if doc.name != doctor_name]

    def add_patient(self, patient):
        self.patients.append(patient)

    def remove_patient(self, patient_name):
        self.patients = [pat for pat in self.patients if pat.name != patient_name]

    def get_doctors(self):
        return [doc.name for doc in self.doctors]

    def get_patients(self):
        return [pat.name for pat in self.patients]


class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty


class Patient:
    def __init__(self, name, disease):
        self.name = name
        self.disease = disease


# Example usage
hospital = Hospital("City Hospital", "Lahore")

# Add doctors
doc1 = Doctor("Dr. Ali", "Cardiology")
doc2 = Doctor("Dr. Sara", "Neurology")
hospital.add_doctor(doc1)
hospital.add_doctor(doc2)

# Add patients
pat1 = Patient("Ahmed", "Flu")
pat2 = Patient("Ayesha", "Migraine")
hospital.add_patient(pat1)
hospital.add_patient(pat2)

print("Doctors in hospital:", hospital.get_doctors())
print("Patients in hospital:", hospital.get_patients())

# Remove a doctor and a patient
hospital.remove_doctor("Dr. Ali")
hospital.remove_patient("Ahmed")

print("Doctors after removal:", hospital.get_doctors())
print("Patients after removal:", hospital.get_patients())
