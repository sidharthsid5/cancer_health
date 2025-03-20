
from django.urls import path
from .views import home, register_patient, register_guest, register_volunteer

urlpatterns = [
    path('', home, name='home'),
    path('register/patient/', register_patient, name='register_patient'),
    path('register/guest/', register_guest, name='register_guest'),
    path('register/volunteer/', register_volunteer, name='register_volunteer'),
]
