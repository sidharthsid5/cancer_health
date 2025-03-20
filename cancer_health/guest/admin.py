# Register your models here.


from .models import Guest, HairDonation, Donation
from django.contrib import admin

admin.site.register(Guest)
admin.site.register(HairDonation)
admin.site.register(Donation)