class HealthReport:
    def __init__(self, report_id, patient_id, content, date):
        self.report_id = report_id
        self.patient_id = patient_id
        self.content = content
        self.date = date

    def __repr__(self):
        return f"<HealthReport {self.report_id}: {self.date}>" 
