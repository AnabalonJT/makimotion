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
    # === APRENDIZAJES GENERALES ===
    aprendizaje_pujo_caca = models.BooleanField(default=False, help_text="Aprendió pujo caca")
    aprendizaje_banquito = models.BooleanField(default=False, help_text="Aprendió uso de banquito")
    aprendizaje_transverso = models.BooleanField(default=False, help_text="Aprendió activación transverso abdominal")
    aprendizaje_respiracion_pelvico = models.BooleanField(default=False, help_text="Aprendió coordinación respiración contracción piso pélvico")
    aprendizaje_contraccion_pelvico = models.BooleanField(default=False, help_text="Aprendió contracción piso pélvico")
    aprendizaje_preapretar = models.BooleanField(default=False, help_text="Aprendió preapretar")
    aprendizaje_otros = models.TextField(blank=True, help_text="Otros aprendizajes generales")

    # === APRENDIZAJES EMBARAZO ===
    aprendizaje_emb_oms = models.BooleanField(default=False, help_text="Aprendió OMS")
    aprendizaje_emb_anatomia = models.BooleanField(default=False, help_text="Aprendió anatomía")
    aprendizaje_emb_movimientos = models.BooleanField(default=False, help_text="Aprendió movimientos cardinales")
    aprendizaje_emb_posicion_trabajo = models.BooleanField(default=False, help_text="Aprendió posición trabajo parto")
    aprendizaje_emb_posicion_expulsion = models.BooleanField(default=False, help_text="Aprendió posición expulsión")
    aprendizaje_emb_intervencion = models.BooleanField(default=False, help_text="Aprendió intervención obstétrica")
    aprendizaje_emb_masaje_perineal = models.BooleanField(default=False, help_text="Aprendió masaje perineal")
    aprendizaje_emb_respiraciones = models.BooleanField(default=False, help_text="Aprendió respiraciones")
    aprendizaje_emb_pujo = models.BooleanField(default=False, help_text="Aprendió pujo embarazo")
    aprendizaje_emb_tecnicas_dolor = models.BooleanField(default=False, help_text="Aprendió técnicas de dolor")
    aprendizaje_emb_otros = models.TextField(blank=True, help_text="Otros aprendizajes embarazo")
    """Ficha clínica para pacientes de piso pélvico"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Profesional responsable")
    
    # === DATOS DEL PACIENTE (Esenciales) ===
    full_name = models.CharField(max_length=200, help_text="Nombre completo del paciente")
    age = models.PositiveIntegerField(help_text="Edad del paciente")
    profession = models.CharField(max_length=100, default="", blank=True, help_text="Profesión")
    address = models.TextField(default="", blank=True, help_text="Dirección")
    phone = models.CharField(max_length=20, default="", blank=True, help_text="Teléfono")
    medications = models.TextField(blank=True, help_text="Medicamentos actuales")
    musculoskeletal_history = models.TextField(blank=True, help_text="Antecedentes músculo esquelético quirúrgico")
    consultation_reason = models.TextField(default="", blank=True, help_text="Motivo de consulta")
    patient_data_other = models.TextField(blank=True, help_text="Otros - Datos del paciente")
    alta = models.BooleanField(default=False, help_text="Indica si el paciente fue dado de alta y se cerró su ciclo clínico.")
    
    # === EMBARAZO ===
    is_pregnant = models.BooleanField(default=False, help_text="¿Está embarazada?")
    pregnancy_weeks_at_registration = models.PositiveIntegerField(null=True, blank=True, help_text="Semanas de embarazo al momento del registro")
    pregnancy_week_day = models.CharField(max_length=10, choices=[
        ('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miércoles'), 
        ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sábado'), ('domingo', 'Domingo')
    ], blank=True, help_text="Día de la semana para contar semanas")
    pregnancy_registration_date = models.DateField(null=True, blank=True, help_text="Fecha cuando se registraron las semanas")
    
    # === ANTECEDENTES GINECOLÓGICOS ===
    menopause = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No')], blank=True, help_text="Menopausia")
    menopause_time = models.CharField(max_length=50, blank=True, help_text="Hace cuánto tiempo")
    regular_menstrual_cycle = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No')], blank=True, help_text="Ciclo menstrual regular")
    previous_surgeries = models.TextField(blank=True, help_text="Cirugías previas")
    pregnancies_g = models.PositiveIntegerField(null=True, blank=True, help_text="G (Gestaciones)")
    abortions_a = models.PositiveIntegerField(null=True, blank=True, help_text="A (Abortos)")
    losses_p = models.PositiveIntegerField(null=True, blank=True, help_text="P (Pérdidas)")
    child_weight = models.TextField(blank=True, help_text="Peso del hijo")
    delivery_type = models.CharField(max_length=50, blank=True, help_text="Partos: normal y/o cesárea")
    episiotomies = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No')], blank=True, help_text="Episiotomías")
    postpartum = models.TextField(blank=True, help_text="Post parto")
    instrumentation = models.TextField(blank=True, help_text="Instrumentalización")
    muscle_tear = models.TextField(blank=True, help_text="Desgarro muscular")
    io = models.BooleanField(default=False, help_text="IO")
    if_field = models.BooleanField(default=False, help_text="IF")
    ig = models.BooleanField(default=False, help_text="IG")
    prolapse = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No')], blank=True, help_text="Prolapso")
    prolapse_type = models.TextField(blank=True, help_text="¿Cuál prolapso?")
    allergies = models.TextField(blank=True, help_text="Alergias")
    gynecological_other = models.TextField(blank=True, help_text="Otros")
    
    # === HÁBITOS DE VIDA ===
    smoking = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No')], blank=True, help_text="Fuma")
    alcohol = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No')], blank=True, help_text="Alcohol")
    physical_activity = models.TextField(blank=True, help_text="Actividad física")
    diet = models.TextField(blank=True, help_text="Dieta")
    daily_liquid_consumption = models.TextField(blank=True, help_text="Consumo líquido diario")
    lifestyle_other = models.TextField(blank=True, help_text="Otros")
    
    # === FUNCIÓN URINARIA ===
    daily_frequency = models.CharField(max_length=50, blank=True, help_text="Frecuencia diaria")
    nocturnal_frequency = models.CharField(max_length=50, blank=True, help_text="Frecuencia nocturna")
    # Checkboxes para síntomas urinarios
    pollakiuria = models.BooleanField(default=False, help_text="Polaquiuria")
    nocturia = models.BooleanField(default=False, help_text="Nocturia")
    urgency = models.BooleanField(default=False, help_text="Urgencia")
    polyuria = models.BooleanField(default=False, help_text="Poliuria")
    dysuria = models.BooleanField(default=False, help_text="Disuria")
    latency = models.BooleanField(default=False, help_text="Latencia")
    effort_to_urinate = models.BooleanField(default=False, help_text="Esfuerzo para orinar")
    incomplete_emptying = models.BooleanField(default=False, help_text="Sensación vaciamiento incompleto")
    immediate_need = models.BooleanField(default=False, help_text="Necesidad inmediata")
    terminal_dripping = models.BooleanField(default=False, help_text="Goteo terminal")
    nocturnal_urgency = models.BooleanField(default=False, help_text="Urgencia nocturna")
    
    urination_position = models.TextField(blank=True, help_text="Micción posición adoptada")
    stream_description = models.TextField(blank=True, help_text="Descripción de chorro")
    urinary_function_other = models.TextField(blank=True, help_text="Otros")
    
    # === INCONTINENCIA ORINA (Subsección) ===
    iue = models.BooleanField(default=False, help_text="IUE")
    iuu = models.BooleanField(default=False, help_text="IUU")
    ium = models.BooleanField(default=False, help_text="IUM")
    iu_posture = models.BooleanField(default=False, help_text="IU postura")
    iu_sensitivity = models.BooleanField(default=False, help_text="IU sensibilidad")
    iu_coital = models.BooleanField(default=False, help_text="IU coital")
    incontinence_other = models.TextField(blank=True, help_text="Otros")
    when_occurs_daily = models.TextField(blank=True, help_text="Cuándo ocurre por día")
    how_daily = models.TextField(blank=True, help_text="Cómo es por día")
    since_when = models.TextField(blank=True, help_text="Hace cuánto")
    during_pregnancy = models.TextField(blank=True, help_text="Durante el embarazo")
    post_pregnancy = models.TextField(blank=True, help_text="Post embarazo")
    prolapse_post_pregnancy = models.TextField(blank=True, help_text="Prolapso post embarazo")
    conscious_urination = models.TextField(blank=True, help_text="Consciente de cuándo quiere orinar")
    containment_capacity = models.TextField(blank=True, help_text="Capacidad de contención")
    protection_type = models.TextField(blank=True, help_text="Algún tipo de protección")
    activities_stopped = models.TextField(blank=True, help_text="Actividad dejada por el problema")
    
    # === FUNCIONAMIENTO INTESTINAL ===
    constipation = models.BooleanField(default=False, help_text="Estreñimiento")
    fecal_incontinence = models.BooleanField(default=False, help_text="Incontinencia")
    gas_incontinence = models.BooleanField(default=False, help_text="Incontinencia gases")
    hemorrhoids = models.BooleanField(default=False, help_text="Hemorroides")
    rectocele = models.BooleanField(default=False, help_text="Rectocele")
    gas_stool_discrimination = models.BooleanField(default=False, help_text="Discriminación gas de caca")
    painful_evacuation = models.BooleanField(default=False, help_text="Evacuación dolorosa")
    straining_defecation = models.BooleanField(default=False, help_text="Puja para defecar")
    complete_evacuation = models.BooleanField(default=False, help_text="Sensación de evacuación completa")
    laxatives = models.BooleanField(default=False, help_text="Laxantes")
    plugging_sensation = models.BooleanField(default=False, help_text="Sensación de tapón")
    
    defecation_position = models.TextField(blank=True, help_text="Posición para hacer caca")
    bristol_scale = models.PositiveIntegerField(null=True, blank=True, help_text="Bristol (1-7)")
    position_frequency = models.TextField(blank=True, help_text="Frecuencia de posiciones")
    bowel_inconsistency = models.TextField(blank=True, help_text="¿Sufre inconsistencia? ¿Cuándo?")
    bowel_conscious = models.TextField(blank=True, help_text="¿Es consciente?")
    bowel_pad = models.TextField(blank=True, help_text="¿Apósito?")
    bowel_activities_stopped = models.TextField(blank=True, help_text="Actividad que dejó por el problema")
    bowel_function_other = models.TextField(blank=True, help_text="Otros")
    
    # === HISTORIAL SEXUAL ===
    sexual_status = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No'), ('virgen', 'Virgen')], blank=True, help_text="Estado sexual")
    urinary_incontinence_sexual = models.BooleanField(default=False, help_text="Incontinencia orina durante sexo")
    urinary_incontinence_sexual_when = models.TextField(blank=True, help_text="¿Cuándo?")
    fecal_incontinence_sexual = models.BooleanField(default=False, help_text="Incontinencia fecal durante sexo")
    fecal_incontinence_sexual_when = models.TextField(blank=True, help_text="¿Cuándo?")
    
    # Síntomas sexuales (checkboxes)
    sexual_desire = models.BooleanField(default=False, help_text="Deseo sexual")
    sexual_excitement = models.BooleanField(default=False, help_text="Excitación")
    orgasm = models.BooleanField(default=False, help_text="Orgasmo")
    dyspareunia = models.BooleanField(default=False, help_text="Dispareunia")
    urge_to_urinate_during_sex = models.BooleanField(default=False, help_text="Siente deseo de orinar durante")
    vaginal_dryness = models.BooleanField(default=False, help_text="Resequedad")
    impaired_by_incontinence = models.BooleanField(default=False, help_text="Perjudicado por incontinencia")
    sexual_history_other = models.TextField(blank=True, help_text="Otros")
    
    # === EXAMEN FÍSICO ===
    diastasis = models.TextField(blank=True, help_text="Diastasis")
    scars = models.TextField(blank=True, help_text="Cicatrices")
    adherences = models.TextField(blank=True, help_text="Adherencias")
    skin_coloration = models.TextField(blank=True, help_text="Coloración de la piel")
    push_exam = models.CharField(max_length=20, choices=[('normal', 'Normal'), ('alterado', 'Alterado')], blank=True, help_text="Pujo")
    
    # NCP - Tono
    ncp_tone_contraction = models.TextField(blank=True, help_text="NCP Tono - Contracción")
    ncp_tone_relaxation = models.TextField(blank=True, help_text="NCP Tono - Relajación")
    ncp_tone_push = models.TextField(blank=True, help_text="NCP Tono - Pujo")
    ncp_tone_pain = models.TextField(blank=True, help_text="NCP Tono - Dolor")
    
    # NCP - Sensibilidad y reflejo (dermatoma s2 s4)
    anal_cutaneous_reflex = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No')], blank=True, help_text="Reflejo cutáneo anal")
    vulvo_cavernous_reflex = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No')], blank=True, help_text="Reflejo vulvo cavernoso")
    cough_reflex = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No')], blank=True, help_text="Reflejo tusígeno")
    physical_exam_other = models.TextField(blank=True, help_text="Otros")
    
    # === EXAMEN INTRACAVITARIO ===
    intracavitary_consent = models.BooleanField(default=False, help_text="Consentimiento")
    intracavitary_scars = models.TextField(blank=True, help_text="Cicatrices")
    intracavitary_mucosa = models.TextField(blank=True, help_text="Mucosa")
    
    # MEA (Músculos del Elevador del Ano)
    mea_tonicity_rest = models.TextField(blank=True, help_text="Tonicidad MEA reposo")
    mea_perception = models.TextField(blank=True, help_text="Percepción MEA")
    mea_contraction = models.TextField(blank=True, help_text="Contracción MEA")
    mea_symmetry_rest = models.TextField(blank=True, help_text="Simetría MEA reposo")
    mea_symmetry_contraction = models.TextField(blank=True, help_text="Simetría MEA contracción")
    mea_voluntary_relaxation = models.TextField(blank=True, help_text="Relajación voluntaria MEA")
    
    # Dolor MEA
    mea_pain_eva = models.PositiveIntegerField(null=True, blank=True, help_text="Dolor MEA - EVA (0-10)")
    mea_pain_location = models.TextField(blank=True, help_text="Dolor MEA - Dónde")
    mea_pain_when = models.TextField(blank=True, help_text="Dolor MEA - Cuándo")
    mea_pain_description = models.TextField(blank=True, help_text="Dolor MEA - Descripción")
    
    # Otros exámenes intracavitarios
    urethral_movement = models.TextField(blank=True, help_text="Movimiento uretral")
    transverse_abdominal_tone = models.TextField(blank=True, help_text="Tono del transverso abdominal")
    oxford_force = models.TextField(blank=True, help_text="Fuerza (Oxford)")
    superficial_musculature = models.TextField(blank=True, help_text="Musculatura superficial")
    deep_musculature = models.TextField(blank=True, help_text="Musculatura profunda")
    intracavitary_exam_other = models.TextField(blank=True, help_text="Otros")
    
    # === EXAMEN COLOPROCTOLÓGICO ===
    coloproctologic_consent = models.BooleanField(default=False, help_text="Consentimiento")
    anal_canal_closure = models.BooleanField(default=False, help_text="Cierre canal anal")
    irritation = models.BooleanField(default=False, help_text="Irritación")
    stool_remains = models.BooleanField(default=False, help_text="Resto de deposiciones")
    rectocele_exam = models.BooleanField(default=False, help_text="Recto cele")
    coloproctologic_scars = models.TextField(blank=True, help_text="Cicatriz, dónde")
    coloproctologic_hemorrhoids = models.TextField(blank=True, help_text="Hemorroides, dónde")
    
    # Tono y resistencia
    rest_tone = models.TextField(blank=True, help_text="Tono en reposo")
    resistance = models.TextField(blank=True, help_text="Resistencia")
    eae_tonicity_rest = models.TextField(blank=True, help_text="Tonicidad EAE reposo")
    eae_contraction = models.TextField(blank=True, help_text="Contracción EAE")
    
    # Oxford
    oxford_anorectal_angle = models.TextField(blank=True, help_text="Ángulo ano rectal")
    oxford_notes = models.TextField(blank=True, help_text="Oxford - Notas")
    
    # Pujo
    anorectal_opening = models.BooleanField(default=False, help_text="Apertura ano rectal")
    thoracic_rectal_synchronization = models.BooleanField(default=False, help_text="Sincronización toraco rectal")
    anal_canal_relaxation = models.BooleanField(default=False, help_text="Relajación canal anal")
    coloproctologic_exam_other = models.TextField(blank=True, help_text="Otros")
    
    # === METADATOS ===
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.full_name} ({self.age} años)"
    
    def get_last_appointment(self):
        """Get the most recent appointment for this patient"""
        return self.appointments.first()
    
    def get_pregnancy_start_date(self):
        """Calculate the pregnancy start date based on weeks and day"""
        if not self.is_pregnant or not self.pregnancy_weeks_at_registration or not self.pregnancy_week_day or not self.pregnancy_registration_date:
            return None
        
        from datetime import timedelta
        
        # Mapeo de días de la semana
        weekday_map = {
            'lunes': 0, 'martes': 1, 'miercoles': 2, 'jueves': 3,
            'viernes': 4, 'sabado': 5, 'domingo': 6
        }
        
        target_weekday = weekday_map.get(self.pregnancy_week_day)
        if target_weekday is None:
            return None
        
        # Encontrar el día de la semana más cercano a la fecha de registro
        registration_date = self.pregnancy_registration_date
        days_since_target = (registration_date.weekday() - target_weekday) % 7
        last_target_day = registration_date - timedelta(days=days_since_target)
        
        # Calcular fecha de inicio del embarazo
        weeks_in_days = self.pregnancy_weeks_at_registration * 7
        pregnancy_start = last_target_day - timedelta(days=weeks_in_days)
        
        return pregnancy_start
    
    def get_current_pregnancy_weeks(self):
        """Calculate current pregnancy weeks"""
        if not self.is_pregnant:
            return None
        
        pregnancy_start = self.get_pregnancy_start_date()
        if not pregnancy_start:
            return self.pregnancy_weeks_at_registration  # Fallback
        
        from django.utils import timezone
        from datetime import timedelta
        
        today = timezone.now().date()
        
        # Mapeo de días de la semana
        weekday_map = {
            'lunes': 0, 'martes': 1, 'miercoles': 2, 'jueves': 3,
            'viernes': 4, 'sabado': 5, 'domingo': 6
        }
        
        target_weekday = weekday_map.get(self.pregnancy_week_day, 0)
        
        # Encontrar el último día de la semana objetivo
        days_since_target = (today.weekday() - target_weekday) % 7
        last_target_day = today - timedelta(days=days_since_target)
        
        # Calcular semanas desde el inicio del embarazo
        days_pregnant = (last_target_day - pregnancy_start).days
        weeks_pregnant = max(0, days_pregnant // 7)
        
        return weeks_pregnant
    
    def get_pregnancy_display(self):
        """Get pregnancy display text"""
        if not self.is_pregnant:
            return None
        
        weeks = self.get_current_pregnancy_weeks()
        if weeks is None:
            return "Embarazada"
        
        return f"🌸 {weeks} semanas"
    
    class Meta:
        ordering = ['full_name']
        verbose_name = "Ficha Clínica"
        verbose_name_plural = "Fichas Clínicas"


class Appointment(models.Model):
    """Appointment model for patient sessions with PERFECT test assessment"""
    YES_NO_CHOICES = [
        ('si', 'Sí'),
        ('no', 'No'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments', help_text="Paciente")
    date_time = models.DateTimeField(help_text="Fecha y hora de la cita")
    session_description = models.TextField(help_text="Descripción de la sesión o actividad realizada")
    additional_notes = models.TextField(blank=True, help_text="Notas adicionales")
    # Tareas o indicaciones dejadas para el paciente (opcional)
    tasks = models.TextField(blank=True, help_text="Tareas o indicaciones para seguimiento")
    
    # PERFECT Test Fields
    perfect_p_power = models.PositiveIntegerField(null=True, blank=True, help_text="P - Power (Fuerza)")
    perfect_e_endurance = models.PositiveIntegerField(null=True, blank=True, help_text="E - Endurance (Resistencia)")
    perfect_r_repetitions = models.PositiveIntegerField(null=True, blank=True, help_text="R - Repetitions (Repeticiones)")
    perfect_f_fast = models.PositiveIntegerField(null=True, blank=True, help_text="F - Fast contractions (Contracciones rápidas)")
    perfect_e_every = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, help_text="E - Every contraction (Cada contracción)")
    perfect_c_cocontraction = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, help_text="C - Co-contraction (Co-contracción)")
    perfect_t_timing = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, help_text="T - Timing (Coordinación)")
    
    # Test del Balón Fields
    balloon_rectal_sensation = models.TextField(blank=True, help_text="Sensación rectal consciente: 10 - 30 ml")
    balloon_first_desire_volume = models.TextField(blank=True, help_text="Volumen Primer deseo: 50 - 60 ml")
    balloon_normal_desire_volume = models.TextField(blank=True, help_text="Volumen Deseo normal constante: sin acomodación 90 - 120ml")
    balloon_max_tolerable_capacity = models.TextField(blank=True, help_text="Capacidad máxima tolerable: máximo tolerable 200-240 ml")
    balloon_rectoanal_reflex = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, help_text="Reflejo rectoanal estriado")
    balloon_expulsion = models.CharField(max_length=10, choices=YES_NO_CHOICES, blank=True, help_text="Expulsión del balón")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient.full_name} - {self.date_time.strftime('%d/%m/%Y %H:%M')}"
    
    def get_perfect_score_display(self):
        """Return formatted PERFECT test results"""
        return {
            'P': self.perfect_p_power,
            'E': self.perfect_e_endurance,
            'R': self.perfect_r_repetitions,
            'F': self.perfect_f_fast,
            'E2': self.perfect_e_every,
            'C': self.perfect_c_cocontraction,
            'T': self.perfect_t_timing,
        }
    
    class Meta:
        ordering = ['-date_time']
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
