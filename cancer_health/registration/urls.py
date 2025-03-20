from django.urls import path
from . import views

urlpatterns = [
    # PatientReg URLs
    path('patient-regs/', views.patient_reg_list_create, name='patient_reg_list_create'),
    path('patient-regs/edit/<int:pk>/', views.patient_reg_edit, name='patient_reg_edit'),
    path('patient-regs/delete/<int:pk>/', views.patient_reg_delete, name='patient_reg_delete'),

    # VolunteerReg URLs
    path('volunteer-regs/', views.volunteer_reg_list_create, name='volunteer_reg_list_create'),
    path('volunteer-regs/edit/<int:pk>/', views.volunteer_reg_edit, name='volunteer_reg_edit'),
    path('volunteer-regs/delete/<int:pk>/', views.volunteer_reg_delete, name='volunteer_reg_delete'),
]