# Register your models here.

from django.contrib import admin
from .models import (
    CancerType, ScanType, ScanCenter, CounCenter,
    HairDonCriteria, MedServices, GuideLines, DietaryTip,
    DietarySupply, Events, Admin, State, Dist
)

admin.site.register(CancerType)
admin.site.register(ScanType)
admin.site.register(ScanCenter)
admin.site.register(CounCenter)
admin.site.register(HairDonCriteria)
admin.site.register(MedServices)
admin.site.register(GuideLines)
admin.site.register(DietaryTip)
admin.site.register(DietarySupply)
admin.site.register(Events)
admin.site.register(Admin)
admin.site.register(State)
admin.site.register(Dist)