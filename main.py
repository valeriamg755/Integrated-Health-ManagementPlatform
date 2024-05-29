from services.appointment_service import AppointmentService
from services.communication_service import CommunicationService
from services.ehr_service import EhrService
from services.medication_service import MedicationService
from services.monitoring_service import MonitoringService
from services.report_service import ReportService
from entities.appointment import Appointment
from entities.patient import Patient
from entities.health_report import HealthReport

# Crear instancias de servicios
appointment_service = AppointmentService()
communication_service = CommunicationService()
ehr_service = EhrService()
medication_service = MedicationService(communication_service)
monitoring_service = MonitoringService()
report_service = ReportService()

# Crear un nuevo paciente
patient = Patient(patient_id=1, name="Valeria Martínez", birth_date="2005-05-07", contact_info="vmartinez@abc.com", medical_history=[])

# Crear una nueva cita
appointment = Appointment(appointment_id=1, patient_id=1, doctor_id=1, date="2024-04-01", time="10:00", status="scheduled")

# Guardar la cita
appointment_service.create_appointment(appointment)

# Enviar una notificación de recordatorio de medicación
medication_service.send_medication_reminder(patient_id=1, message="Recordatorio: tomar la medicación a las 8:00 AM")

# Obtener y actualizar registros médicos del paciente
ehr_service.update_patient_records(patient_id=1, records=["Nuevo registro médico"])

# Generar un reporte de salud
health_report = HealthReport(report_id=1, patient_id=1, content="Reporte de salud del paciente", date="2024-06-06")
report_service.generate_health_report(health_report)

# Imprimir resultados
print(f"Cita creada: {appointment}")
print(f"Notificaciones: {communication_service.get_notifications(patient_id=1)}")
print(f"Registros médicos actualizados: {ehr_service.get_patient_records(patient_id=1)}")
print(f"Reportes de salud: {report_service.get_health_reports(patient_id=1)}")
