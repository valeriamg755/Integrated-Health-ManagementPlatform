from entities.iot_device import IotDevice

class MonitoringService:
    def __init__(self):
        self.device_data = []
    
    def add_device_data(self, device_data):
        self.device_data.append(device_data)
    
    def get_device_data(self, patient_id, device_type):
        return [d for d in self.device_data if d.patient_id == patient_id and d.type == device_type]
