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
                'placeholder': 'Nombre completo del paciente'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad',
                'min': 0,
                'max': 120
            }),
            'diagnosis': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Diagnóstico o condición principal',
                'rows': 3
            }),
            'general_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Notas generales (opcional)',
                'rows': 4
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
                'type': 'datetime-local'
            }),
            'session_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción de la sesión o actividad realizada',
                'rows': 4
            }),
            'evaluation': forms.Select(attrs={
                'class': 'form-control'
            }),
            'additional_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Notas adicionales (opcional)',
                'rows': 3
            }),
        }
        labels = {
            'date_time': 'Fecha y Hora',
            'session_description': 'Descripción de la Sesión',
            'evaluation': 'Evaluación del Progreso',
            'additional_notes': 'Notas Adicionales',
        }
    
    def clean_session_description(self):
        """Validate session description is not empty"""
        session_description = self.cleaned_data.get('session_description', '').strip()
        if not session_description:
            raise forms.ValidationError("La descripción de la sesión es requerida.")
        return session_description