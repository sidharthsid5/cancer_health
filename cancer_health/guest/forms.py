from django import forms
from .models import HairDonation, Donation



class HairDonationForm(forms.ModelForm):
    class Meta:
        model = HairDonation
        fields = 'Hair_type','Hair_image'

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = 'Amount', 'Description'