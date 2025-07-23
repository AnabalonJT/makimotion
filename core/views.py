from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Max
from .models import Patient, Appointment
from .forms import PatientForm, AppointmentForm

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


@login_required
def patient_create(request):
    """Create a new patient"""
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user  # Associate with current user
            patient.save()
            messages.success(request, f'Paciente {patient.full_name} creado exitosamente.')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm()
    
    return render(request, 'patients/patient_form.html', {'form': form})


@login_required
def patient_detail(request, pk):
    """View patient details with appointment history"""
    patient = get_object_or_404(Patient, pk=pk, user=request.user)
    appointments = patient.appointments.all()
    
    context = {
        'patient': patient,
        'appointments': appointments,
    }
    return render(request, 'patients/patient_detail.html', context)


@login_required
def patient_update(request, pk):
    """Update patient information"""
    patient = get_object_or_404(Patient, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, f'Información de {patient.full_name} actualizada exitosamente.')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    
    return render(request, 'patients/patient_form.html', {'form': form})


@login_required
def patient_delete(request, pk):
    """Delete patient with confirmation"""
    patient = get_object_or_404(Patient, pk=pk, user=request.user)
    
    if request.method == 'POST':
        patient_name = patient.full_name
        appointment_count = patient.appointments.count()
        patient.delete()
        messages.success(request, f'Paciente {patient_name} y sus {appointment_count} citas han sido eliminados.')
        return redirect('dashboard')
    
    context = {
        'patient': patient,
        'appointment_count': patient.appointments.count(),
    }
    return render(request, 'patients/patient_confirm_delete.html', context)
