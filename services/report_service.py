from entities.health_report import HealthReport

class ReportService:
    def __init__(self):
        self.reports = []
    
    def generate_health_report(self, report):
        self.reports.append(report)
    
    def get_health_reports(self, patient_id):
        return [r for r in self.reports if r.patient_id == patient_id]
