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
        fields = ['id','Name', 'Address', 'District', 'Age', 'Gender', 'Photo', 'Cancer_Type', 'Detected_Date',
                  'Detected_Hospital', 'Consult_Doctor', 'No_months_per_year', 'Stage', 'Status', 'Email', 'Mobile']

# Guest Registration Form
class GuestRegistrationForm(forms.ModelForm):
    Username = forms.CharField(max_length=10)
    Password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(max_length=10, widget=forms.PasswordInput)

    class Meta:
        model = Guest
        fields = ['Name', 'Address', 'District', 'Phone', 'Mobile', 'Email']

# Volunteer Registration Form
class VolunteerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['id', 'Apply_area', 'Location']
