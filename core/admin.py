from django.contrib import admin
from .models import UserProfile, Patient, Appointment


class AppointmentInline(admin.TabularInline):
    """Inline appointments for patient admin"""
    model = Appointment
    extra = 0
    fields = ('date_time', 'session_description', 'perfect_p_power', 'perfect_e_endurance')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin configuration for UserProfile"""
    list_display = ('user', 'practice_name', 'license_number', 'created_at')
    search_fields = ('user__username', 'practice_name', 'license_number')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Admin configuration for Patient"""
    list_display = ('full_name', 'age', 'user', 'created_at', 'appointment_count')
    search_fields = ('full_name', 'profession', 'user__username')
    list_filter = ('user', 'birth_date', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [AppointmentInline]
    
    def appointment_count(self, obj):
        """Display appointment count for each patient"""
        return obj.appointments.count()
    appointment_count.short_description = 'Citas'


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """Admin configuration for Appointment with PERFECT test fields"""
    list_display = ('patient', 'date_time', 'perfect_summary', 'created_at')
    search_fields = ('patient__full_name', 'session_description', 'additional_notes')
    list_filter = ('date_time', 'patient__user', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'date_time'
    fieldsets = (
        ('Información General', {
            'fields': ('patient', 'date_time', 'session_description', 'additional_notes')
        }),
        ('Test PERFECT', {
            'fields': (
                ('perfect_p_power', 'perfect_e_endurance', 'perfect_r_repetitions', 'perfect_f_fast'),
                ('perfect_e_every', 'perfect_c_cocontraction', 'perfect_t_timing')
            )
        }),
        ('Metadatos', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def perfect_summary(self, obj):
        """Display PERFECT test summary"""
        scores = obj.get_perfect_score_display()
        return f"P:{scores['P']} E:{scores['E']} R:{scores['R']} F:{scores['F']}"
    perfect_summary.short_description = 'Test PERFECT'
    
    def get_queryset(self, request):
        """Optimize queries with select_related"""
        return super().get_queryset(request).select_related('patient', 'patient__user')
