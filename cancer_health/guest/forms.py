from django import forms
from .models import Guest, HairDonation, Donation

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'

class HairDonationForm(forms.ModelForm):
    class Meta:
        model = HairDonation
        fields = '__all__'

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'