from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    CancerType, ScanType, ScanCenter, CounCenter,
    HairDonCriteria, MedServices, GuideLines, DietaryTip,
    DietarySupply, Events, State, Dist
)
from .forms import (
    CancerTypeForm, ScanTypeForm, ScanCenterForm, CounCenterForm,
    HairDonCriteriaForm, MedServicesForm, GuideLinesForm, DietaryTipForm,
    DietarySupplyForm, EventsForm, StateForm, DistForm
)
def homes(request):
    # return HttpResponse("hai<br>"
    #                     "<a href='cancer_type_list_create'>Click me</a><br>"
    #                     "<a href='state_list_create'>Click me</a><br>"
    #                     "<a href='dist_list_create'>Click me</a><br>"
    #                     "<a href='scan_type_list_create'>Click me</a><br>"
    #                     "<a href='scan_center_list_create'>Click me</a><br>"
    #                     "<a href='coun_center_list_create'>Click me</a><br>"
    #                     "<a href='hair_don_criteria_list_create'>Click me</a><br>"
    #                     "<a href='med_services_list_create'>Click me</a><br>"
    #                     "<a href='guide_lines_list_create'>Click me</a><br>"
    #                     "<a href='dietary_tip_list_create'>Click me</a><br>"
    #                     "<a href='dietary_supply_list_create'>Click me</a><br>"
    #                     "<a href='events_list_create'>Click me</a><br>"
    #                     )
    return render(request,'admin_home.html')
# CancerType
def cancer_type_list_create(request):
    if request.method == 'POST':
        form = CancerTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cancer_type_list_create')
    else:
        form = CancerTypeForm()
    cancer_types = CancerType.objects.all()
    return render(request, 'cancer_type_list_create.html', {'form': form, 'cancer_types': cancer_types})

def cancer_type_edit(request, pk):
    cancer_type = get_object_or_404(CancerType, pk=pk)
    if request.method == 'POST':
        form = CancerTypeForm(request.POST, instance=cancer_type)
        if form.is_valid():
            form.save()
            return redirect('cancer_type_list_create')
    else:
        form = CancerTypeForm(instance=cancer_type)
    return render(request, 'cancer_type_edit.html', {'form': form})

def cancer_type_delete(request, pk):
    cancer_type = get_object_or_404(CancerType, pk=pk)
    if request.method == 'POST':
        cancer_type.delete()
        return redirect('cancer_type_list_create')
    return render(request, 'cancer_type_delete.html', {'cancer_type': cancer_type})


# State
def state_list_create(request):
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('state_list_create')
    else:
        form = StateForm()
    states = State.objects.all()
    return render(request, 'state_list_create.html', {'form': form, 'states': states})

def state_edit(request, pk):
    state = get_object_or_404(State, pk=pk)
    if request.method == 'POST':
        form = StateForm(request.POST, instance=state)
        if form.is_valid():
            form.save()
            return redirect('state_list_create')
    else:
        form = StateForm(instance=state)
    return render(request, 'state_edit.html', {'form': form})

def state_delete(request, pk):
    state = get_object_or_404(State, pk=pk)
    if request.method == 'POST':
        state.delete()
        return redirect('state_list_create')
    return render(request, 'state_delete.html', {'state': state})

# Dist
def dist_list_create(request):
    if request.method == 'POST':
        form = DistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dist_list_create')
    else:
        form = DistForm()
    dists = Dist.objects.all()
    return render(request, 'dist_list_create.html', {'form': form, 'dists': dists})

def dist_edit(request, pk):
    dist = get_object_or_404(Dist, pk=pk)
    if request.method == 'POST':
        form = DistForm(request.POST, instance=dist)
        if form.is_valid():
            form.save()
            return redirect('dist_list_create')
    else:
        form = DistForm(instance=dist)
    return render(request, 'dist_edit.html', {'form': form})

def dist_delete(request, pk):
    dist = get_object_or_404(Dist, pk=pk)
    if request.method == 'POST':
        dist.delete()
        return redirect('dist_list_create')
    return render(request, 'dist_delete.html', {'dist': dist})
# ScanType
def scan_type_list_create(request):
    if request.method == 'POST':
        form = ScanTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scan_type_list_create')
    else:
        form = ScanTypeForm()
    scan_types = ScanType.objects.all()
    return render(request, 'scan_type_list_create.html', {'form': form, 'scan_types': scan_types})

def scan_type_edit(request, pk):
    scan_type = get_object_or_404(ScanType, pk=pk)
    if request.method == 'POST':
        form = ScanTypeForm(request.POST, instance=scan_type)
        if form.is_valid():
            form.save()
            return redirect('scan_type_list_create')
    else:
        form = ScanTypeForm(instance=scan_type)
    return render(request, 'scan_type_edit.html', {'form': form})

def scan_type_delete(request, pk):
    scan_type = get_object_or_404(ScanType, pk=pk)
    if request.method == 'POST':
        scan_type.delete()
        return redirect('scan_type_list_create')
    return render(request, 'scan_type_delete.html', {'scan_type': scan_type})

# ScanCenter
def scan_center_list_create(request):
    if request.method == 'POST':
        form = ScanCenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scan_center_list_create')
    else:
        form = ScanCenterForm()
    scan_centers = ScanCenter.objects.all()
    return render(request, 'scan_center_list_create.html', {'form': form, 'scan_centers': scan_centers})

def scan_center_edit(request, pk):
    scan_center = get_object_or_404(ScanCenter, pk=pk)
    if request.method == 'POST':
        form = ScanCenterForm(request.POST, instance=scan_center)
        if form.is_valid():
            form.save()
            return redirect('scan_center_list_create')
    else:
        form = ScanCenterForm(instance=scan_center)
    return render(request, 'scan_center_edit.html', {'form': form})

def scan_center_delete(request, pk):
    scan_center = get_object_or_404(ScanCenter, pk=pk)
    if request.method == 'POST':
        scan_center.delete()
        return redirect('scan_center_list_create')
    return render(request, 'scan_center_delete.html', {'scan_center': scan_center})

# CounCenter
def coun_center_list_create(request):
    if request.method == 'POST':
        form = CounCenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coun_center_list_create')
    else:
        form = CounCenterForm()
    coun_centers = CounCenter.objects.all()
    return render(request, 'coun_center_list_create.html', {'form': form, 'coun_centers': coun_centers})

def coun_center_edit(request, pk):
    coun_center = get_object_or_404(CounCenter, pk=pk)
    if request.method == 'POST':
        form = CounCenterForm(request.POST, instance=coun_center)
        if form.is_valid():
            form.save()
            return redirect('coun_center_list_create')
    else:
        form = CounCenterForm(instance=coun_center)
    return render(request, 'coun_center_edit.html', {'form': form})

def coun_center_delete(request, pk):
    coun_center = get_object_or_404(CounCenter, pk=pk)
    if request.method == 'POST':
        coun_center.delete()
        return redirect('coun_center_list_create')
    return render(request, 'coun_center_delete.html', {'coun_center': coun_center})

# HairDonCriteria
def hair_don_criteria_list_create(request):
    if request.method == 'POST':
        form = HairDonCriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hair_don_criteria_list_create')
    else:
        form = HairDonCriteriaForm()
    hair_don_criterias = HairDonCriteria.objects.all()
    return render(request, 'hair_don_criteria_list_create.html', {'form': form, 'hair_don_criterias': hair_don_criterias})

def hair_don_criteria_edit(request, pk):
    hair_don_criteria = get_object_or_404(HairDonCriteria, pk=pk)
    if request.method == 'POST':
        form = HairDonCriteriaForm(request.POST, instance=hair_don_criteria)
        if form.is_valid():
            form.save()
            return redirect('hair_don_criteria_list_create')
    else:
        form = HairDonCriteriaForm(instance=hair_don_criteria)
    return render(request, 'hair_don_criteria_edit.html', {'form': form})

def hair_don_criteria_delete(request, pk):
    hair_don_criteria = get_object_or_404(HairDonCriteria, pk=pk)
    if request.method == 'POST':
        hair_don_criteria.delete()
        return redirect('hair_don_criteria_list_create')
    return render(request, 'hair_don_criteria_delete.html', {'hair_don_criteria': hair_don_criteria})

# MedServices
def med_services_list_create(request):
    if request.method == 'POST':
        form = MedServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('med_services_list_create')
    else:
        form = MedServicesForm()
    med_services = MedServices.objects.all()
    return render(request, 'med_services_list_create.html', {'form': form, 'med_services': med_services})

def med_services_edit(request, pk):
    med_service = get_object_or_404(MedServices, pk=pk)
    if request.method == 'POST':
        form = MedServicesForm(request.POST, instance=med_service)
        if form.is_valid():
            form.save()
            return redirect('med_services_list_create')
    else:
        form = MedServicesForm(instance=med_service)
    return render(request, 'med_services_edit.html', {'form': form})

def med_services_delete(request, pk):
    med_service = get_object_or_404(MedServices, pk=pk)
    if request.method == 'POST':
        med_service.delete()
        return redirect('med_services_list_create')
    return render(request, 'med_services_delete.html', {'med_service': med_service})

# GuideLines
def guide_lines_list_create(request):
    if request.method == 'POST':
        form = GuideLinesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guide_lines_list_create')
    else:
        form = GuideLinesForm()
    guide_lines = GuideLines.objects.all()
    return render(request, 'guide_lines_list_create.html', {'form': form, 'guide_lines': guide_lines})

def guide_lines_edit(request, pk):
    guide_line = get_object_or_404(GuideLines, pk=pk)
    if request.method == 'POST':
        form = GuideLinesForm(request.POST, instance=guide_line)
        if form.is_valid():
            form.save()
            return redirect('guide_lines_list_create')
    else:
        form = GuideLinesForm(instance=guide_line)
    return render(request, 'guide_lines_edit.html', {'form': form})

def guide_lines_delete(request, pk):
    guide_line = get_object_or_404(GuideLines, pk=pk)
    if request.method == 'POST':
        guide_line.delete()
        return redirect('guide_lines_list_create')
    return render(request, 'guide_lines_delete.html', {'guide_line': guide_line})

# DietaryTip
def dietary_tip_list_create(request):
    if request.method == 'POST':
        form = DietaryTipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dietary_tip_list_create')
    else:
        form = DietaryTipForm()
    dietary_tips = DietaryTip.objects.all()
    return render(request, 'dietary_tip_list_create.html', {'form': form, 'dietary_tips': dietary_tips})

def dietary_tip_edit(request, pk):
    dietary_tip = get_object_or_404(DietaryTip, pk=pk)
    if request.method == 'POST':
        form = DietaryTipForm(request.POST, instance=dietary_tip)
        if form.is_valid():
            form.save()
            return redirect('dietary_tip_list_create')
    else:
        form = DietaryTipForm(instance=dietary_tip)
    return render(request, 'dietary_tip_edit.html', {'form': form})

def dietary_tip_delete(request, pk):
    dietary_tip = get_object_or_404(DietaryTip, pk=pk)
    if request.method == 'POST':
        dietary_tip.delete()
        return redirect('dietary_tip_list_create')
    return render(request, 'dietary_tip_delete.html', {'dietary_tip': dietary_tip})

# DietarySupply
def dietary_supply_list_create(request):
    if request.method == 'POST':
        form = DietarySupplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dietary_supply_list_create')
    else:
        form = DietarySupplyForm()
    dietary_supplies = DietarySupply.objects.all()
    return render(request, 'dietary_supply_list_create.html', {'form': form, 'dietary_supplies': dietary_supplies})

def dietary_supply_edit(request, pk):
    dietary_supply = get_object_or_404(DietarySupply, pk=pk)
    if request.method == 'POST':
        form = DietarySupplyForm(request.POST, instance=dietary_supply)
        if form.is_valid():
            form.save()
            return redirect('dietary_supply_list_create')
    else:
        form = DietarySupplyForm(instance=dietary_supply)
    return render(request, 'dietary_supply_edit.html', {'form': form})

def dietary_supply_delete(request, pk):
    dietary_supply = get_object_or_404(DietarySupply, pk=pk)
    if request.method == 'POST':
        dietary_supply.delete()
        return redirect('dietary_supply_list_create')
    return render(request, 'dietary_supply_delete.html', {'dietary_supply': dietary_supply})

# Events
def events_list_create(request):
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events_list_create')
    else:
        form = EventsForm()
    events = Events.objects.all()
    return render(request, 'events_list_create.html', {'form': form, 'events': events})

def events_edit(request, pk):
    event = get_object_or_404(Events, pk=pk)
    if request.method == 'POST':
        form = EventsForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events_list_create')
    else:
        form = EventsForm(instance=event)
    return render(request, 'events_edit.html', {'form': form})

def events_delete(request, pk):
    event = get_object_or_404(Events, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('events_list_create')
    return render(request, 'events_delete.html', {'event': event})