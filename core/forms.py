from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Patient, Appointment


class CustomUserCreationForm(UserCreationForm):
    """Custom user registration form with additional fields"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com'
        })
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apellido'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes to password fields
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class PatientForm(forms.ModelForm):
    """Form for creating and editing clinical records for pelvic floor patients"""
    
    class Meta:
        model = Patient
        fields = [
            # Datos del paciente (esenciales)
            'full_name', 'age', 'profession', 'address', 'phone', 
            'medications', 'musculoskeletal_history', 'consultation_reason', 'patient_data_other', 'alta',
            
            # Embarazo
            'is_pregnant', 'pregnancy_weeks_at_registration', 'pregnancy_week_day',
            
            # Antecedentes ginecológicos
            'menopause', 'menopause_time', 'regular_menstrual_cycle', 'previous_surgeries',
            'pregnancies_g', 'abortions_a', 'losses_p', 'child_weight', 'delivery_type',
            'episiotomies', 'postpartum', 'instrumentation', 'muscle_tear',
            'io', 'if_field', 'ig', 'prolapse', 'prolapse_type', 'allergies', 'gynecological_other',
            
            # Hábitos de vida
            'smoking', 'alcohol', 'physical_activity', 'diet', 'daily_liquid_consumption', 'lifestyle_other',
            
            # Función urinaria
            'daily_frequency', 'nocturnal_frequency',
            'pollakiuria', 'nocturia', 'urgency', 'polyuria', 'dysuria', 'latency',
            'effort_to_urinate', 'incomplete_emptying', 'immediate_need', 'terminal_dripping', 'nocturnal_urgency',
            'urination_position', 'stream_description', 'urinary_function_other',
            
            # Incontinencia orina
            'iue', 'iuu', 'ium', 'iu_posture', 'iu_sensitivity', 'iu_coital', 'incontinence_other',
            'when_occurs_daily', 'how_daily', 'since_when', 'during_pregnancy', 'post_pregnancy',
            'prolapse_post_pregnancy', 'conscious_urination', 'containment_capacity', 'protection_type', 'activities_stopped',
            
            # Funcionamiento intestinal
            'constipation', 'fecal_incontinence', 'gas_incontinence', 'hemorrhoids', 'rectocele',
            'gas_stool_discrimination', 'painful_evacuation', 'straining_defecation',
            'complete_evacuation', 'laxatives', 'plugging_sensation',
            'defecation_position', 'bristol_scale', 'position_frequency', 'bowel_inconsistency', 'bowel_conscious', 'bowel_pad', 'bowel_activities_stopped', 'bowel_function_other',
            
            # Historial sexual
            'sexual_status', 'urinary_incontinence_sexual', 'urinary_incontinence_sexual_when',
            'fecal_incontinence_sexual', 'fecal_incontinence_sexual_when',
            'sexual_desire', 'sexual_excitement', 'orgasm', 'dyspareunia', 'urge_to_urinate_during_sex', 'vaginal_dryness', 'impaired_by_incontinence', 'sexual_history_other',
            
            # Examen físico
            'diastasis', 'scars', 'adherences', 'skin_coloration', 'push_exam',
            'ncp_tone_contraction', 'ncp_tone_relaxation', 'ncp_tone_push', 'ncp_tone_pain',
            'anal_cutaneous_reflex', 'vulvo_cavernous_reflex', 'cough_reflex', 'physical_exam_other',
            
            # Examen intracavitario
            'intracavitary_consent', 'intracavitary_scars', 'intracavitary_mucosa',
            'mea_tonicity_rest', 'mea_perception', 'mea_contraction', 'mea_symmetry_rest', 'mea_symmetry_contraction', 'mea_voluntary_relaxation',
            'mea_pain_eva', 'mea_pain_location', 'mea_pain_when', 'mea_pain_description',
            'urethral_movement', 'transverse_abdominal_tone', 'oxford_force', 'superficial_musculature', 'deep_musculature', 'intracavitary_exam_other',
            
            # Examen coloproctológico
            'coloproctologic_consent', 'anal_canal_closure', 'irritation', 'stool_remains', 'rectocele_exam',
            'coloproctologic_scars', 'coloproctologic_hemorrhoids',
            'rest_tone', 'resistance', 'eae_tonicity_rest', 'eae_contraction',
            'oxford_anorectal_angle', 'oxford_notes', 'anorectal_opening', 'thoracic_rectal_synchronization', 'anal_canal_relaxation', 'coloproctologic_exam_other'
        ]
        
        widgets = {
            # Datos del paciente
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'min': 0, 'max': 120}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'required': True, 'rows': 2}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'medications': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'musculoskeletal_history': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'consultation_reason': forms.Textarea(attrs={'class': 'form-control', 'required': True, 'rows': 3}),
            'patient_data_other': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'alta': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
            # Embarazo
            'pregnancy_weeks_at_registration': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 42, 'placeholder': 'Ej: 12'}),
            'pregnancy_week_day': forms.Select(attrs={'class': 'form-control'}),
            
            # Antecedentes ginecológicos
            'menopause': forms.Select(attrs={'class': 'form-control'}),
            'menopause_time': forms.TextInput(attrs={'class': 'form-control'}),
            'regular_menstrual_cycle': forms.Select(attrs={'class': 'form-control'}),
            'previous_surgeries': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'pregnancies_g': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'abortions_a': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'losses_p': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'child_weight': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_type': forms.TextInput(attrs={'class': 'form-control'}),
            'episiotomies': forms.Select(attrs={'class': 'form-control'}),
            'postpartum': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'instrumentation': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'muscle_tear': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'prolapse': forms.Select(attrs={'class': 'form-control'}),
            'prolapse_type': forms.TextInput(attrs={'class': 'form-control'}),
            'allergies': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'gynecological_other': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            
            # Hábitos de vida
            'smoking': forms.Select(attrs={'class': 'form-control'}),
            'alcohol': forms.Select(attrs={'class': 'form-control'}),
            'physical_activity': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'diet': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'daily_liquid_consumption': forms.TextInput(attrs={'class': 'form-control'}),
            'lifestyle_other': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            
            # Función urinaria
            'daily_frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'nocturnal_frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'urination_position': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'stream_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'urinary_function_other': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            
            # Incontinencia
            'incontinence_other': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'when_occurs_daily': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'how_daily': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'since_when': forms.TextInput(attrs={'class': 'form-control'}),
            'during_pregnancy': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'post_pregnancy': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'prolapse_post_pregnancy': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'conscious_urination': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'containment_capacity': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'protection_type': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'activities_stopped': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            
            # Funcionamiento intestinal
            'defecation_position': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'bristol_scale': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 7}),
            'bowel_inconsistency': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'bowel_conscious': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'bowel_pad': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'bowel_activities_stopped': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'bowel_function_other': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'position_frequency': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            
            # Historial sexual
            'sexual_status': forms.Select(attrs={'class': 'form-control'}),
            'urinary_incontinence_sexual_when': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'fecal_incontinence_sexual_when': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'sexual_history_other': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            
            # Examen físico
            'diastasis': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'scars': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'adherences': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'skin_coloration': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'push_exam': forms.Select(attrs={'class': 'form-control'}),
            'ncp_tone_contraction': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'ncp_tone_relaxation': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'ncp_tone_push': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'ncp_tone_pain': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'anal_cutaneous_reflex': forms.Select(attrs={'class': 'form-control'}),
            'vulvo_cavernous_reflex': forms.Select(attrs={'class': 'form-control'}),
            'cough_reflex': forms.Select(attrs={'class': 'form-control'}),
            'physical_exam_other': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            
            # Examen intracavitario
            'intracavitary_scars': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'intracavitary_mucosa': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'mea_tonicity_rest': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'mea_perception': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'mea_contraction': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'mea_symmetry_rest': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'mea_symmetry_contraction': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'mea_voluntary_relaxation': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'mea_pain_eva': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 10}),
            'mea_pain_location': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'mea_pain_when': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'mea_pain_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'urethral_movement': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'transverse_abdominal_tone': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'oxford_force': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'superficial_musculature': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'deep_musculature': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'intracavitary_exam_other': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            
            # Examen coloproctológico
            'coloproctologic_scars': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'coloproctologic_hemorrhoids': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'rest_tone': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'resistance': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'eae_tonicity_rest': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'eae_contraction': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'oxford_anorectal_angle': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'oxford_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'coloproctologic_exam_other': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
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
    
    def clean_consultation_reason(self):
        """Validate consultation reason is not empty"""
        consultation_reason = self.cleaned_data.get('consultation_reason', '').strip()
        if not consultation_reason:
            raise forms.ValidationError("El motivo de consulta es requerido.")
        return consultation_reason
    
    def save(self, commit=True):
        """Save the patient and set pregnancy registration date if needed"""
        patient = super().save(commit=False)
        
        # Si está embarazada y tiene semanas registradas, establecer fecha de registro
        if patient.is_pregnant and patient.pregnancy_weeks_at_registration and not patient.pregnancy_registration_date:
            from django.utils import timezone
            patient.pregnancy_registration_date = timezone.now().date()
        
        # Si ya no está embarazada, limpiar campos de embarazo
        if not patient.is_pregnant:
            patient.pregnancy_weeks_at_registration = None
            patient.pregnancy_week_day = ''
            patient.pregnancy_registration_date = None
        
        if commit:
            patient.save()
        return patient


class AppointmentForm(forms.ModelForm):
    """Form for creating and editing appointments with PERFECT test assessment"""
    
    class Meta:
        model = Appointment
        fields = [
            'date_time',
            'session_description',
            'additional_notes',
            'tasks',
            # PERFECT Test fields
            'perfect_p_power',
            'perfect_e_endurance',
            'perfect_r_repetitions',
            'perfect_f_fast',
            'perfect_e_every',
            'perfect_c_cocontraction',
            'perfect_t_timing',
            # Test del Balón fields
            'balloon_rectal_sensation',
            'balloon_first_desire_volume',
            'balloon_normal_desire_volume',
            'balloon_max_tolerable_capacity',
            'balloon_rectoanal_reflex',
            'balloon_expulsion',
        ]
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
                'maxlength': 1000
            }),
            'additional_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Notas adicionales (opcional)',
                'rows': 3,
                'maxlength': 500
            }),
            # PERFECT Test widgets
            'perfect_p_power': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 10,
                'placeholder': 'Ej: 3'
            }),
            'perfect_e_endurance': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 10,
                'placeholder': 'Ej: 5'
            }),
            'perfect_r_repetitions': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 10,
                'placeholder': 'Ej: 8'
            }),
            'perfect_f_fast': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 10,
                'placeholder': 'Ej: 4'
            }),
            'perfect_e_every': forms.Select(attrs={
                'class': 'form-control'
            }),
            'perfect_c_cocontraction': forms.Select(attrs={
                'class': 'form-control'
            }),
            'perfect_t_timing': forms.Select(attrs={
                'class': 'form-control'
            }),
            # Test del Balón widgets
            'balloon_rectal_sensation': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Ej: 15 ml'
            }),
            'balloon_first_desire_volume': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Ej: 55 ml'
            }),
            'balloon_normal_desire_volume': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Ej: 100 ml'
            }),
            'balloon_max_tolerable_capacity': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Ej: 220 ml'
            }),
            'balloon_rectoanal_reflex': forms.Select(attrs={
                'class': 'form-control'
            }),
            'balloon_expulsion': forms.Select(attrs={
                'class': 'form-control'
            }),
            'tasks': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Tareas o indicaciones para el paciente (opcional)'
            }),
        }
        labels = {
            'date_time': 'Fecha y Hora',
            'session_description': 'Descripción de la Sesión',
            'additional_notes': 'Notas Adicionales',
            # PERFECT Test labels
            'perfect_p_power': 'P - Power (Fuerza)',
            'perfect_e_endurance': 'E - Endurance (Resistencia)',
            'perfect_r_repetitions': 'R - Repetitions (Repeticiones)',
            'perfect_f_fast': 'F - Fast contractions (Contracciones rápidas)',
            'perfect_e_every': 'E - Every contraction (Cada contracción)',
            'perfect_c_cocontraction': 'C - Co-contraction (Co-contracción)',
            'perfect_t_timing': 'T - Timing (Coordinación)',
            # Test del Balón labels
            'balloon_rectal_sensation': 'Sensación rectal consciente',
            'balloon_first_desire_volume': 'Volumen Primer deseo',
            'balloon_normal_desire_volume': 'Volumen Deseo normal constante',
            'balloon_max_tolerable_capacity': 'Capacidad máxima tolerable',
            'balloon_rectoanal_reflex': 'Reflejo rectoanal estriado',
            'balloon_expulsion': 'Expulsión del balón',
        }
    
    def clean_session_description(self):
        """Validate session description is not empty and has reasonable length"""
        session_description = self.cleaned_data.get('session_description', '').strip()
        if not session_description:
            raise forms.ValidationError("La descripción de la sesión es requerida.")
        if len(session_description) > 1000:
            raise forms.ValidationError("La descripción no puede exceder 1000 caracteres.")
        return session_description
    
    def clean_date_time(self):
        """Validate appointment date and time"""
        from django.utils import timezone
        date_time = self.cleaned_data.get('date_time')
        # NOTE: allow past dates because clinicians may register past appointments
        if date_time:
            # Only restrict excessively far future dates (2 years)
            now = timezone.now()
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
    
    def clean_perfect_p_power(self):
        """Validate P (Power) field"""
        value = self.cleaned_data.get('perfect_p_power')
        if value is not None and (value < 0 or value > 10):
            raise forms.ValidationError("El valor debe estar entre 0 y 10.")
        return value
    
    def clean_perfect_e_endurance(self):
        """Validate E (Endurance) field"""
        value = self.cleaned_data.get('perfect_e_endurance')
        if value is not None and (value < 0 or value > 10):
            raise forms.ValidationError("El valor debe estar entre 0 y 10.")
        return value
    
    def clean_perfect_r_repetitions(self):
        """Validate R (Repetitions) field"""
        value = self.cleaned_data.get('perfect_r_repetitions')
        if value is not None and (value < 0 or value > 10):
            raise forms.ValidationError("El valor debe estar entre 0 y 10.")
        return value
    
    def clean_perfect_f_fast(self):
        """Validate F (Fast contractions) field"""
        value = self.cleaned_data.get('perfect_f_fast')
        if value is not None and (value < 0 or value > 10):
            raise forms.ValidationError("El valor debe estar entre 0 y 10.")
        return value