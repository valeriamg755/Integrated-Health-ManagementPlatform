from entities.notification import Notification

class MedicationService:
    def __init__(self, communication_service):
        self.communication_service = communication_service
    
    def send_medication_reminder(self, patient_id, message):
        notification_id = len(self.communication_service.notifications) + 1
        notification = Notification(notification_id=notification_id, patient_id=patient_id, message=message, date="2024-05-01")
        self.communication_service.send_notification(notification)
    
    def get_medication_reminders(self, patient_id):
        return self.communication_service.get_notifications(patient_id)
