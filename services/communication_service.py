from entities.notification import Notification

class CommunicationService:
    def __init__(self):
        self.notifications = []
    
    def send_notification(self, notification):
        self.notifications.append(notification)
    
    def get_notifications(self, patient_id):
        return [n for n in self.notifications if n.patient_id == patient_id]
