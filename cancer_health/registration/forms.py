from django import forms
from .models import PatientReg, VolunteerReg

class PatientRegForm(forms.ModelForm):
    class Meta:
        model = PatientReg
        fields = '__all__'

class VolunteerRegForm(forms.ModelForm):
    class Meta:
        model = VolunteerReg
        fields = '__all__'