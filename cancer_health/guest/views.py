from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import HairDonationForm, DonationForm
from .models import HairDonation, Donation
from login.forms import GuestRegistrationForm
from login.models import Guest

def homeee(request):
    # return HttpResponse("hai<br>"
    #                     "<a href='hair_donation_list_create'>Click me</a><br>"
    #                     "<a href='donation_list_create'>Click me</a><br>"
    #
    #                     )
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
        form = HairDonationForm(request.POST)
        if form.is_valid():
            form.save()
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