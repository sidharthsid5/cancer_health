
from django.urls import path
from .views import home, register_patient, register_guest, register_volunteer, login1

urlpatterns = [
    path('', home, name='home'),
    path('register_patient/', register_patient, name='register_patient'),
    path('register_guest/', register_guest, name='register_guest'),
    path('register_volunteer/', register_volunteer, name='register_volunteer'),
    path('login/',login1,name='login1')
]
