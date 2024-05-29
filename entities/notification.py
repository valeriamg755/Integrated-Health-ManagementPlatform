class Notification:
    def __init__(self, notification_id, patient_id, message, date):
        self.notification_id = notification_id
        self.patient_id = patient_id
        self.message = message
        self.date = date

    def __repr__(self):
        return f"<Notification {self.notification_id}: {self.date}>"
