from entities.appointment import Appointment

class AppointmentService:
    def __init__(self):
        self.appointments = []
    
    def create_appointment(self, appointment):
        self.appointments.append(appointment)
    
    def cancel_appointment(self, appointment_id):
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                appointment.status = 'cancelled'
    
    def reschedule_appointment(self, appointment_id, new_date, new_time):
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                appointment.date = new_date
                appointment.time = new_time
