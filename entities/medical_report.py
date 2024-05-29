class MedicalReport:
    def __init__(self, report_id, patient_id, doctor_id, content, date):
        self.report_id = report_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.content = content
        self.date = date

    def __repr__(self):
        return f"<MedicalReport {self.report_id}: {self.date}>"
