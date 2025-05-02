from django import forms
from .models import HairDonation, Donation



class HairDonationForm(forms.ModelForm):
    class Meta:
        model = HairDonation
        fields = '__all__'

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'