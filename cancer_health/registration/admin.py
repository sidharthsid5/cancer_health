# Register your models here.


from django.contrib import admin
from .models import PatientReg, VolunteerReg

admin.site.register(PatientReg)
admin.site.register(VolunteerReg)