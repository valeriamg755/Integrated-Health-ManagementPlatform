class EhrService:
    def __init__(self):
        self.records = {}
    
    def get_patient_records(self, patient_id):
        return self.records.get(patient_id, [])
    
    def update_patient_records(self, patient_id, records):
        if patient_id not in self.records:
            self.records[patient_id] = []
        self.records[patient_id].extend(records)
