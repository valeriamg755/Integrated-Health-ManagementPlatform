class Patient:
    def __init__(self, patient_id, name, birth_date, contact_info, medical_history):
        self.patient_id = patient_id
        self.name = name
        self.birth_date = birth_date
        self.contact_info = contact_info
        self.medical_history = medical_history

    def __repr__(self):
        return f"<Patient {self.patient_id}: {self.name}>"
