from django import forms
from .models import (
    CancerType, ScanType, ScanCenter, CounCenter,
    HairDonCriteria, MedServices, GuideLines, DietaryTip,
    DietarySupply, Events, Admin, State, Dist
)

class CancerTypeForm(forms.ModelForm):
    class Meta:
        model = CancerType
        fields = '__all__'

class ScanTypeForm(forms.ModelForm):
    class Meta:
        model = ScanType
        fields = '__all__'

class ScanCenterForm(forms.ModelForm):
    class Meta:
        model = ScanCenter
        fields = '__all__'

class CounCenterForm(forms.ModelForm):
    class Meta:
        model = CounCenter
        fields = '__all__'

class HairDonCriteriaForm(forms.ModelForm):
    class Meta:
        model = HairDonCriteria
        fields = '__all__'

class MedServicesForm(forms.ModelForm):
    class Meta:
        model = MedServices
        fields = '__all__'

class GuideLinesForm(forms.ModelForm):
    class Meta:
        model = GuideLines
        fields = '__all__'

class DietaryTipForm(forms.ModelForm):
    class Meta:
        model = DietaryTip
        fields = '__all__'

class DietarySupplyForm(forms.ModelForm):
    class Meta:
        model = DietarySupply
        fields = '__all__'

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

class DistForm(forms.ModelForm):
    class Meta:
        model = Dist
        fields = '__all__'