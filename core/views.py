from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Max, Q
from .models import Patient, Appointment, FichaClinica

@login_required
def patient_list(request):
    """Lista de todos los pacientes (dados de alta y no) con barra de búsqueda"""
    query = request.GET.get('q', '')
    patients = Patient.objects.filter(user=request.user)
    if query and len(query) >= 2:
        patients = patients.filter(full_name__icontains=query)
    patients = patients.order_by('-alta', '-full_name')
    total_patients = patients.count()
    context = {
        'patients': patients,
        'total_patients': total_patients,
        'query': query,
    }
    return render(request, 'patients/patient_list.html', context)
from .forms import PatientForm, AppointmentForm, FichaClinicaForm

@login_required
def dashboard(request):
    """Dashboard view showing patient overview with sorting"""
    # Get sorting parameter
    sort_by = request.GET.get('sort', 'name')
    sort_order = request.GET.get('order', 'asc')
    
    # Get user's patients que no han sido dados de alta
    patients = Patient.objects.filter(user=request.user, alta=False)
    
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
        ).order_by('-last_appointment')
    
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
    """View patient details with appointment history and latest clinical record"""
    patient = get_object_or_404(Patient, pk=pk, user=request.user)
    appointments = patient.appointments.all()
    
    # Get the latest clinical record
    latest_ficha = patient.get_last_ficha_clinica()
    
    # Get the latest 3 clinical records for the header (ordered by fecha)
    recent_fichas = patient.fichas_clinicas.order_by('-fecha', '-created_at')[:3]
    
    context = {
        'patient': patient,
        'appointments': appointments,
        'latest_ficha': latest_ficha,
        'recent_fichas': recent_fichas,
    }
    return render(request, 'patients/patient_detail.html', context)


@login_required
def patient_update(request, pk):
    """Update patient information"""
    patient = get_object_or_404(Patient, pk=pk, user=request.user)
    
    if request.method == 'POST':
        print(request.POST)  # Debugging line to check POST data
        # Si solo se envía el campo 'alta' y csrf, actualizar directamente sin usar el formulario
        if set(request.POST.keys()) == {'csrfmiddlewaretoken', 'alta'} and request.POST.get('alta') == 'true':
            patient.alta = True
            patient.save()
            messages.success(request, f'Paciente {patient.full_name} fue dado de alta.')
            return redirect('patient_detail', pk=patient.pk)
        else:
            form = PatientForm(request.POST, instance=patient)
            if form.is_valid():
                paciente = form.save()
                messages.success(request, f'Información de {paciente.full_name} actualizada exitosamente.')
                return redirect('patient_detail', pk=paciente.pk)
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


@login_required
def appointment_create(request, patient_id):
    """Create a new appointment for a specific patient"""
    patient = get_object_or_404(Patient, pk=patient_id, user=request.user)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            messages.success(request, f'Cita para {patient.full_name} creada exitosamente.')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = AppointmentForm()
    
    context = {
        'form': form,
        'patient': patient,
    }
    return render(request, 'appointments/appointment_form.html', context)


@login_required
def appointment_update(request, pk):
    """Update appointment information"""
    appointment = get_object_or_404(Appointment, pk=pk, patient__user=request.user)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cita de {appointment.patient.full_name} actualizada exitosamente.')
            return redirect('patient_detail', pk=appointment.patient.pk)
    else:
        form = AppointmentForm(instance=appointment)
    
    context = {
        'form': form,
        'patient': appointment.patient,
    }
    return render(request, 'appointments/appointment_form.html', context)


@login_required
def appointment_detail(request, pk):
    """View appointment details"""
    appointment = get_object_or_404(Appointment, pk=pk, patient__user=request.user)
    
    context = {
        'appointment': appointment,
        'patient': appointment.patient,
    }
    return render(request, 'appointments/appointment_detail.html', context)


@login_required
def appointment_delete(request, pk):
    """Delete appointment with confirmation"""
    appointment = get_object_or_404(Appointment, pk=pk, patient__user=request.user)
    patient = appointment.patient
    
    if request.method == 'POST':
        appointment_date = appointment.date_time.strftime('%d/%m/%Y %H:%M')
        appointment.delete()
        messages.success(request, f'Cita del {appointment_date} para {patient.full_name} ha sido eliminada.')
        return redirect('patient_detail', pk=patient.pk)
    
    context = {
        'appointment': appointment,
        'patient': patient,
    }
    return render(request, 'appointments/appointment_confirm_delete.html', context)


# ==============================================
# FICHAS CLÍNICAS VIEWS
# ==============================================

@login_required
def ficha_clinica_list(request, patient_pk):
    """List all clinical records for a patient"""
    patient = get_object_or_404(Patient, pk=patient_pk, user=request.user)
    fichas = patient.fichas_clinicas.all()
    
    context = {
        'patient': patient,
        'fichas': fichas,
    }
    return render(request, 'fichas_clinicas/ficha_clinica_list.html', context)


@login_required
def ficha_clinica_detail(request, patient_pk, pk):
    """View clinical record details"""
    patient = get_object_or_404(Patient, pk=patient_pk, user=request.user)
    ficha = get_object_or_404(FichaClinica, pk=pk, patient=patient)
    
    context = {
        'patient': patient,
        'ficha': ficha,
    }
    return render(request, 'fichas_clinicas/ficha_clinica_detail.html', context)


@login_required
def ficha_clinica_create(request, patient_pk):
    """Create a new clinical record for a patient"""
    patient = get_object_or_404(Patient, pk=patient_pk, user=request.user)
    
    if request.method == 'POST':
        form = FichaClinicaForm(request.POST)
        if form.is_valid():
            ficha = form.save(commit=False)
            ficha.patient = patient
            ficha.save()
            messages.success(request, f'Nueva ficha clínica creada para {patient.full_name}.')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = FichaClinicaForm()
    
    context = {
        'form': form,
        'patient': patient,
        'title': 'Nueva Ficha Clínica',
    }
    return render(request, 'fichas_clinicas/ficha_clinica_form.html', context)


@login_required
def ficha_clinica_update(request, patient_pk, pk):
    """Update an existing clinical record"""
    patient = get_object_or_404(Patient, pk=patient_pk, user=request.user)
    ficha = get_object_or_404(FichaClinica, pk=pk, patient=patient)
    
    if request.method == 'POST':
        form = FichaClinicaForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ficha clínica de {patient.full_name} actualizada exitosamente.')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = FichaClinicaForm(instance=ficha)
    
    context = {
        'form': form,
        'patient': patient,
        'ficha': ficha,
        'title': 'Editar Ficha Clínica',
    }
    return render(request, 'fichas_clinicas/ficha_clinica_form.html', context)


@login_required
def ficha_clinica_delete(request, patient_pk, pk):
    """Delete a clinical record"""
    patient = get_object_or_404(Patient, pk=patient_pk, user=request.user)
    ficha = get_object_or_404(FichaClinica, pk=pk, patient=patient)
    
    if request.method == 'POST':
        ficha_date = ficha.created_at.strftime('%d/%m/%Y')
        ficha.delete()
        messages.success(request, f'Ficha clínica del {ficha_date} para {patient.full_name} ha sido eliminada.')
        return redirect('patient_detail', pk=patient.pk)
    
    context = {
        'ficha': ficha,
        'patient': patient,
    }
    return render(request, 'fichas_clinicas/ficha_clinica_confirm_delete.html', context)
