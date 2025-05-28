from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import HairDonationForm, DonationForm
from .models import HairDonation, Donation
from login.forms import GuestRegistrationForm
from login.models import Guest

from administrator.models import HairDonCriteria, GuideLines



def homeee(request):
    return render(request, 'guest_home.html')

# Guest
def guest_edit(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        form = GuestRegistrationForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('guest_list_create')
    else:
        form = GuestRegistrationForm(instance=guest)
    return render(request, 'guest_edit.html', {'form': form})

def guest_delete(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        guest.delete()
        return redirect('guest_list_create')
    return render(request, 'guest_delete.html', {'guest': guest})

# HairDonation
def hair_donation_list_create(request):
    if request.method == 'POST':
        form = HairDonationForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.Guest = Guest.objects.get(id=request.session["Guest_id"])
            obj.save()
            return redirect('hair_donation_list_create')
    else:
        form = HairDonationForm()
    hair_donations = HairDonation.objects.all()
    return render(request, 'hair_donation_list_create.html', {'form': form, 'hair_donations': hair_donations})

def hair_donation_edit(request, pk):
    hair_donation = get_object_or_404(HairDonation, pk=pk)
    if request.method == 'POST':
        form = HairDonationForm(request.POST, instance=hair_donation)
        if form.is_valid():
            form.save()
            return redirect('hair_donation_list_create')
    else:
        form = HairDonationForm(instance=hair_donation)
    return render(request, 'hair_donation_edit.html', {'form': form})

def hair_donation_delete(request, pk):
    hair_donation = get_object_or_404(HairDonation, pk=pk)
    if request.method == 'POST':
        hair_donation.delete()
        return redirect('hair_donation_list_create')
    return render(request, 'hair_donation_delete.html', {'hair_donation': hair_donation})

# Donation
def donation_list_create(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_list_create')
    else:
        form = DonationForm()
    donations = Donation.objects.all()
    return render(request, 'donation_list_create.html', {'form': form, 'donations': donations})

def donation_edit(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    if request.method == 'POST':
        form = DonationForm(request.POST, instance=donation)
        if form.is_valid():
            form.save()
            return redirect('donation_list_create')
    else:
        form = DonationForm(instance=donation)
    return render(request, 'donation_edit.html', {'form': form})

def donation_delete(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    if request.method == 'POST':
        donation.delete()
        return redirect('donation_list_create')
    return render(request, 'donation_delete.html', {'donation': donation})


#View Hair donation Criteria
def hair_criteria_view(request):
    context = {
        'donations' : HairDonCriteria.objects.all()
    }
    return render(request,'view_haircriteria.html',context)
def hair_criteria_and_donation_view(request):
    selected_criteria = []
    guest_id = request.session.get("Guest_id")
    show_revealed_content = False

    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_criteria')
        selected_criteria = HairDonCriteria.objects.filter(id__in=selected_ids)
        show_revealed_content = True

        form = HairDonationForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.Guest = Guest.objects.get(id=guest_id)
            obj.save()
            form = HairDonationForm()

    else:
        form = HairDonationForm()

    donations = HairDonCriteria.objects.all()
    hair_donations = HairDonation.objects.filter(Guest_id=guest_id)

    return render(request, 'hair_criteria_and_donation.html', {
        'donations': donations,
        'selected_criteria': selected_criteria,
        'form': form,
        'hair_donations': hair_donations,
        'show_revealed_content': show_revealed_content
    })

# View Guidlines
def guidelines_guest_view(request):
    context={}
    context['dataset']= GuideLines.objects.all()
    return render(request, 'guidlines_guest.html',context)


def donation_list_create(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.Guest = Guest.objects.get(id=request.session["Guest_id"])
            donation.Status = "Initiated"
            donation.save()
            return redirect('fake_payment_portal', donation_id=donation.id)
    else:
        form = DonationForm()

    donations = Donation.objects.filter(Payment_status='Success')
    return render(request, 'donation_list_create.html', {'form': form, 'donations': donations})


def fake_payment_portal(request, donation_id):
    donation = get_object_or_404(Donation, pk=donation_id)
    if request.method == 'POST':
        donation.Payment_status = 'Success'
        donation.Status = 'Completed'
        donation.Transaction_type = 'Card'
        donation.Card_number = 1234567890  # Fake entry
        donation.Bank = 'ABC'
        donation.save()

        return redirect('donation_list_create')
    return render(request, 'fake_payment.html', {'donation': donation})
