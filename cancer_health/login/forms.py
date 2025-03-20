from django import forms
from django.contrib.auth.models import User
from .models import Patient, Guest, Volunteer

# Patient Registration Form
class PatientRegistrationForm(forms.ModelForm):
    Username = forms.CharField(max_length=10)
    Password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(max_length=10, widget=forms.PasswordInput)

    class Meta:
        model = Patient
        fields = ['Patname', 'Address', 'Distid', 'Age', 'Gender', 'Photo', 'cancTypeid', 'DetectedDate',
                  'DetectedHospital', 'Consult_Drname', 'No_months_yr', 'Stage', 'Regdate', 'Status', 'Email', 'Mob']

# Guest Registration Form
class GuestRegistrationForm(forms.ModelForm):
    Username = forms.CharField(max_length=10)
    Password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(max_length=10, widget=forms.PasswordInput)

    class Meta:
        model = Guest
        fields = ['Name', 'Address', 'Distid', 'Regdate', 'Phone', 'Mob', 'Email']

# Volunteer Registration Form
class VolunteerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['Guestid', 'Regdate', 'apply_area', 'want_loc', 'Status']
