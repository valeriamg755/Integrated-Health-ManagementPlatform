class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time, status):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.status = status

    def __repr__(self):
        return f"<Appointment {self.appointment_id}: {self.date} at {self.time}>"
