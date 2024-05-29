class IotDevice:
    def __init__(self, device_id, patient_id, type, data):
        self.device_id = device_id
        self.patient_id = patient_id
        self.type = type
        self.data = data

    def __repr__(self):
        return f"<IotDevice {self.device_id}: {self.type}>"
