from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from .models import Patient, Appointment

@login_required
def dashboard(request):
    """Dashboard view showing patient overview with sorting"""
    # Get sorting parameter
    sort_by = request.GET.get('sort', 'name')
    sort_order = request.GET.get('order', 'asc')
    
    # Get user's patients
    patients = Patient.objects.filter(user=request.user)
    
    # Apply sorting
    if sort_by == 'name':
        if sort_order == 'desc':
            patients = patients.order_by('-full_name')
        else:
            patients = patients.order_by('full_name')
    elif sort_by == 'appointment':
        # Sort by last appointment date
        patients = patients.annotate(
            last_appointment=Max('appointments__date_time')
        )
        if sort_order == 'desc':
            patients = patients.order_by('-last_appointment')
        else:
            patients = patients.order_by('last_appointment')
    
    # Get some statistics
    total_patients = patients.count()
    recent_appointments = Appointment.objects.filter(
        patient__user=request.user
    ).order_by('-date_time')[:5]
    
    context = {
        'user': request.user,
        'patients': patients,
        'total_patients': total_patients,
        'recent_appointments': recent_appointments,
        'current_sort': sort_by,
        'current_order': sort_order,
    }
    
    return render(request, 'dashboard/dashboard.html', context)
