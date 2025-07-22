from django.contrib import admin
from .models import UserProfile, Patient, Appointment


class AppointmentInline(admin.TabularInline):
    """Inline appointments for patient admin"""
    model = Appointment
    extra = 0
    fields = ('date_time', 'evaluation', 'session_description')
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
    search_fields = ('full_name', 'diagnosis', 'user__username')
    list_filter = ('user', 'age', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [AppointmentInline]
    
    def appointment_count(self, obj):
        """Display appointment count for each patient"""
        return obj.appointments.count()
    appointment_count.short_description = 'Citas'


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """Admin configuration for Appointment"""
    list_display = ('patient', 'date_time', 'evaluation', 'created_at')
    search_fields = ('patient__full_name', 'session_description', 'additional_notes')
    list_filter = ('evaluation', 'date_time', 'patient__user', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'date_time'
    
    def get_queryset(self, request):
        """Optimize queries with select_related"""
        return super().get_queryset(request).select_related('patient', 'patient__user')
