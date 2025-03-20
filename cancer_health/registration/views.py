from django.shortcuts import render, redirect, get_object_or_404
from .models import PatientReg, VolunteerReg
from .forms import PatientRegForm, VolunteerRegForm

# PatientReg
def patient_reg_list_create(request):
    if request.method == 'POST':
        form = PatientRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_reg_list_create')
    else:
        form = PatientRegForm()
    patient_regs = PatientReg.objects.all()
    return render(request, 'patient_reg_list_create.html', {'form': form, 'patient_regs': patient_regs})

def patient_reg_edit(request, pk):
    patient_reg = get_object_or_404(PatientReg, pk=pk)
    if request.method == 'POST':
        form = PatientRegForm(request.POST, instance=patient_reg)
        if form.is_valid():
            form.save()
            return redirect('patient_reg_list_create')
    else:
        form = PatientRegForm(instance=patient_reg)
    return render(request, 'patient_reg_edit.html', {'form': form})

def patient_reg_delete(request, pk):
    patient_reg = get_object_or_404(PatientReg, pk=pk)
    if request.method == 'POST':
        patient_reg.delete()
        return redirect('patient_reg_list_create')
    return render(request, 'patient_reg_delete.html', {'patient_reg': patient_reg})

# VolunteerReg
def volunteer_reg_list_create(request):
    if request.method == 'POST':
        form = VolunteerRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteer_reg_list_create')
    else:
        form = VolunteerRegForm()
    volunteer_regs = VolunteerReg.objects.all()
    return render(request, 'volunteer_reg_list_create.html', {'form': form, 'volunteer_regs': volunteer_regs})

def volunteer_reg_edit(request, pk):
    volunteer_reg = get_object_or_404(VolunteerReg, pk=pk)
    if request.method == 'POST':
        form = VolunteerRegForm(request.POST, instance=volunteer_reg)
        if form.is_valid():
            form.save()
            return redirect('volunteer_reg_list_create')
    else:
        form = VolunteerRegForm(instance=volunteer_reg)
    return render(request, 'volunteer_reg_edit.html', {'form': form})

def volunteer_reg_delete(request, pk):
    volunteer_reg = get_object_or_404(VolunteerReg, pk=pk)
    if request.method == 'POST':
        volunteer_reg.delete()
        return redirect('volunteer_reg_list_create')
    return render(request, 'volunteer_reg_delete.html', {'volunteer_reg': volunteer_reg})