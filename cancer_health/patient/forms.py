from django import forms
from .models import ApplyScan, CounsellingBook, RegFreevig, Comments, PatHealthRec


class PatHealthRecForm(forms.ModelForm):
    class Meta:
        model = PatHealthRec
        fields = 'Records_Details','Previous_hospital','Treat_file'

class ApplyScanForm(forms.ModelForm):
    class Meta:
        model = ApplyScan
        fields = '__all__'

class CounsellingBookForm(forms.ModelForm):
    class Meta:
        model = CounsellingBook
        fields = 'Booking_date','Times_lot'

class RegFreevigForm(forms.ModelForm):
    class Meta:
        model = RegFreevig
        fields = ['Full_Name', 'Age', 'Gender', 'Phone', 'Address']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comments',)