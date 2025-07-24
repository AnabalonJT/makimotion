from django import forms
from .models import Patient, Appointment


class PatientForm(forms.ModelForm):
    """Form for creating and editing patients"""
    
    class Meta:
        model = Patient
        fields = ['full_name', 'age', 'diagnosis', 'general_notes']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo del paciente',
                'required': True,
                'minlength': 2,
                'maxlength': 200
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad',
                'min': 0,
                'max': 120,
                'required': True
            }),
            'diagnosis': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Diagnóstico o condición principal',
                'rows': 3,
                'required': True,
                'maxlength': 1000
            }),
            'general_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Notas generales (opcional)',
                'rows': 4,
                'maxlength': 1000
            }),
        }
        labels = {
            'full_name': 'Nombre Completo',
            'age': 'Edad',
            'diagnosis': 'Diagnóstico',
            'general_notes': 'Notas Generales',
        }
    
    def clean_age(self):
        """Validate age is within reasonable range"""
        age = self.cleaned_data.get('age')
        if age is not None:
            if age < 0:
                raise forms.ValidationError("La edad no puede ser negativa.")
            if age > 120:
                raise forms.ValidationError("Por favor ingresa una edad válida.")
        return age
    
    def clean_full_name(self):
        """Validate full name is not empty and has reasonable length"""
        full_name = self.cleaned_data.get('full_name', '').strip()
        if not full_name:
            raise forms.ValidationError("El nombre completo es requerido.")
        if len(full_name) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return full_name
    
    def clean_diagnosis(self):
        """Validate diagnosis is not empty"""
        diagnosis = self.cleaned_data.get('diagnosis', '').strip()
        if not diagnosis:
            raise forms.ValidationError("El diagnóstico es requerido.")
        return diagnosis


class AppointmentForm(forms.ModelForm):
    """Form for creating and editing appointments"""
    
    class Meta:
        model = Appointment
        fields = ['date_time', 'session_description', 'evaluation', 'additional_notes']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'required': True
            }),
            'session_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción de la sesión o actividad realizada',
                'rows': 4,
                'required': True,
                'minlength': 10,
                'maxlength': 1000
            }),
            'evaluation': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'additional_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Notas adicionales (opcional)',
                'rows': 3,
                'maxlength': 500
            }),
        }
        labels = {
            'date_time': 'Fecha y Hora',
            'session_description': 'Descripción de la Sesión',
            'evaluation': 'Evaluación del Progreso',
            'additional_notes': 'Notas Adicionales',
        }
    
    def clean_session_description(self):
        """Validate session description is not empty and has reasonable length"""
        session_description = self.cleaned_data.get('session_description', '').strip()
        if not session_description:
            raise forms.ValidationError("La descripción de la sesión es requerida.")
        if len(session_description) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        if len(session_description) > 1000:
            raise forms.ValidationError("La descripción no puede exceder 1000 caracteres.")
        return session_description
    
    def clean_date_time(self):
        """Validate appointment date and time"""
        from django.utils import timezone
        date_time = self.cleaned_data.get('date_time')
        if date_time:
            # Check if appointment is not in the past (allow some tolerance for editing)
            now = timezone.now()
            if date_time < now - timezone.timedelta(hours=1):
                raise forms.ValidationError("No se pueden programar citas en el pasado.")
            
            # Check if appointment is not too far in the future (2 years)
            max_future = now + timezone.timedelta(days=730)
            if date_time > max_future:
                raise forms.ValidationError("No se pueden programar citas con más de 2 años de anticipación.")
        
        return date_time
    
    def clean_additional_notes(self):
        """Validate additional notes length if provided"""
        additional_notes = self.cleaned_data.get('additional_notes', '').strip()
        if additional_notes and len(additional_notes) > 500:
            raise forms.ValidationError("Las notas adicionales no pueden exceder 500 caracteres.")
        return additional_notes