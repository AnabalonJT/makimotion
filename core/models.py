from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Extended user profile for healthcare professionals"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    practice_name = models.CharField(max_length=200, blank=True, help_text="Nombre de la práctica o clínica")
    license_number = models.CharField(max_length=100, blank=True, help_text="Número de licencia profesional")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"


class Patient(models.Model):
    """Patient model for healthcare management"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Profesional responsable")
    full_name = models.CharField(max_length=200, help_text="Nombre completo del paciente")
    age = models.PositiveIntegerField(help_text="Edad del paciente")
    diagnosis = models.TextField(help_text="Diagnóstico o condición principal")
    general_notes = models.TextField(blank=True, help_text="Notas generales sobre el paciente")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.full_name} ({self.age} años)"
    
    def get_last_appointment(self):
        """Get the most recent appointment for this patient"""
        return self.appointments.first()  # Will work after Appointment model is created
    
    class Meta:
        ordering = ['full_name']
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class Appointment(models.Model):
    """Appointment model for patient sessions"""
    EVALUATION_CHOICES = [
        ('excellent', 'Excelente Progreso'),
        ('good', 'Buen Progreso'),
        ('fair', 'Progreso Regular'),
        ('poor', 'Necesita Atención'),
        ('critical', 'Atención Crítica Requerida'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments', help_text="Paciente")
    date_time = models.DateTimeField(help_text="Fecha y hora de la cita")
    session_description = models.TextField(help_text="Descripción de la sesión o actividad realizada")
    evaluation = models.CharField(max_length=20, choices=EVALUATION_CHOICES, help_text="Evaluación del progreso")
    additional_notes = models.TextField(blank=True, help_text="Notas adicionales")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient.full_name} - {self.date_time.strftime('%d/%m/%Y %H:%M')}"
    
    def get_evaluation_display_color(self):
        """Return CSS class for evaluation display"""
        color_map = {
            'excellent': 'success',
            'good': 'info',
            'fair': 'warning',
            'poor': 'danger',
            'critical': 'critical'
        }
        return color_map.get(self.evaluation, 'secondary')
    
    class Meta:
        ordering = ['-date_time']
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
