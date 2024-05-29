class Doctor:
    def __init__(self, doctor_id, name, specialty, contact_info):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.contact_info = contact_info

    def __repr__(self):
        return f"<Doctor {self.doctor_id}: {self.name}, {self.specialty}>"
