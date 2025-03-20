from django import forms
from .models import PatHealthRec, ApplyScan, CounsellingBook, RegFreevig, Comments

class PatHealthRecForm(forms.ModelForm):
    class Meta:
        model = PatHealthRec
        fields = '__all__'

class ApplyScanForm(forms.ModelForm):
    class Meta:
        model = ApplyScan
        fields = '__all__'

class CounsellingBookForm(forms.ModelForm):
    class Meta:
        model = CounsellingBook
        fields = '__all__'

class RegFreevigForm(forms.ModelForm):
    class Meta:
        model = RegFreevig
        fields = '__all__'

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'