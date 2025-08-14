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
    
    # === HÁBITOS DE VIDA ===
    smoking = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No')], blank=True, help_text="Fuma")
    alcohol = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No')], blank=True, help_text="Alcohol")
    physical_activity = models.TextField(blank=True, help_text="Actividad física")
    diet = models.TextField(blank=True, help_text="Dieta")
    daily_liquid_consumption = models.TextField(blank=True, help_text="Consumo líquido diario")
    
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
    position_frequency = models.BooleanField(default=False, help_text="Frecuencia de posiciones")
    gas_stool_discrimination = models.BooleanField(default=False, help_text="Discriminación gas de caca")
    painful_evacuation = models.BooleanField(default=False, help_text="Evacuación dolorosa")
    straining_defecation = models.BooleanField(default=False, help_text="Puja para defecar")
    complete_evacuation = models.BooleanField(default=False, help_text="Sensación de evacuación completa")
    laxatives = models.BooleanField(default=False, help_text="Laxantes")
    plugging_sensation = models.BooleanField(default=False, help_text="Sensación de tapón")
    
    defecation_position = models.TextField(blank=True, help_text="Posición para hacer caca")
    bristol_scale = models.PositiveIntegerField(null=True, blank=True, help_text="Bristol (1-7)")
    bowel_inconsistency = models.TextField(blank=True, help_text="¿Sufre inconsistencia? ¿Cuándo?")
    bowel_conscious = models.TextField(blank=True, help_text="¿Es consciente?")
    bowel_pad = models.TextField(blank=True, help_text="¿Apósito?")
    bowel_activities_stopped = models.TextField(blank=True, help_text="Actividad que dejó por el problema")
    
    # === HISTORIAL SEXUAL ===
    sexually_active = models.BooleanField(default=False, help_text="Activo sexualmente")
    sexually_active_when = models.TextField(blank=True, help_text="¿Cuándo?")
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
    
    # === EXAMEN FÍSICO ===
    diastasis = models.TextField(blank=True, help_text="Diastasis")
    scars = models.TextField(blank=True, help_text="Cicatrices")
    adherences = models.TextField(blank=True, help_text="Adherencias")
    skin_coloration = models.TextField(blank=True, help_text="Coloración de la piel")
    push_exam = models.CharField(max_length=20, choices=[('normal', 'Normal'), ('alterado', 'Alterado')], blank=True, help_text="Pujo")
    
    # NLP - Tono
    nlp_tone_contraction = models.TextField(blank=True, help_text="NLP Tono - Contracción")
    nlp_tone_relaxation = models.TextField(blank=True, help_text="NLP Tono - Relajación")
    nlp_tone_push = models.TextField(blank=True, help_text="NLP Tono - Pujo")
    nlp_tone_pain = models.TextField(blank=True, help_text="NLP Tono - Dolor")
    
    # NLP - Sensibilidad y reflejo (dermatoma s2 s4)
    anal_cutaneous_reflex = models.BooleanField(default=False, help_text="Reflejo cutáneo anal")
    vulvo_cavernous_reflex = models.BooleanField(default=False, help_text="Reflejo vulvo cavernoso")
    cough_reflex = models.BooleanField(default=False, help_text="Reflejo tusígeno")
    
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
    transverse_urethral_tone = models.TextField(blank=True, help_text="Tono del transverso uretral")
    oxford_force = models.TextField(blank=True, help_text="Fuerza (Oxford)")
    superficial_muscle = models.TextField(blank=True, help_text="Muscular superficial")
    deep_musculature = models.TextField(blank=True, help_text="Musculatura profunda")
    
    # === EXAMEN COLOPROCTOLÓGICO ===
    coloproctologic_consent = models.BooleanField(default=False, help_text="Consentimiento")
    anal_canal_closure = models.BooleanField(default=False, help_text="Cierre canal anal")
    irritation = models.BooleanField(default=False, help_text="Irritación")
    stool_remains = models.BooleanField(default=False, help_text="Resto de deposiciones")
    blind_rectum = models.BooleanField(default=False, help_text="Recto ciego")
    coloproctologic_scars = models.TextField(blank=True, help_text="Cicatriz, dónde")
    coloproctologic_hemorrhoids = models.TextField(blank=True, help_text="Hemorroides, dónde")
    
    # Tono y resistencia
    rest_tone = models.TextField(blank=True, help_text="Tono en reposo")
    resistance = models.TextField(blank=True, help_text="Resistencia")
    eae_tonicity_rest = models.TextField(blank=True, help_text="Tonicidad EAE reposo")
    eae_contraction = models.TextField(blank=True, help_text="Contracción EAE")
    
    # Oxford
    oxford_anorectal_angle = models.TextField(blank=True, help_text="Ángulo ano rectal")
    
    # Empujo
    anorectal_opening = models.BooleanField(default=False, help_text="Apertura ano rectal")
    rectal_torso_synchronization = models.BooleanField(default=False, help_text="Sincronización torso rectal")
    anal_canal_relaxation = models.BooleanField(default=False, help_text="Relajación canal anal")
    
    # === METADATOS ===
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.full_name} ({self.age} años)"
    
    def get_last_appointment(self):
        """Get the most recent appointment for this patient"""
        return self.appointments.first()
    
    class Meta:
        ordering = ['full_name']
        verbose_name = "Ficha Clínica"
        verbose_name_plural = "Fichas Clínicas"


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
