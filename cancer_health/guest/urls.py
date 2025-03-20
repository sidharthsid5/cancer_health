from django.urls import path
from . import views

urlpatterns = [
    # Guest URLs
    path('guests/', views.guest_list_create, name='guest_list_create'),
    path('guests/edit/<int:pk>/', views.guest_edit, name='guest_edit'),
    path('guests/delete/<int:pk>/', views.guest_delete, name='guest_delete'),

    # HairDonation URLs
    path('hair-donations/', views.hair_donation_list_create, name='hair_donation_list_create'),
    path('hair-donations/edit/<int:pk>/', views.hair_donation_edit, name='hair_donation_edit'),
    path('hair-donations/delete/<int:pk>/', views.hair_donation_delete, name='hair_donation_delete'),

    # Donation URLs
    path('donations/', views.donation_list_create, name='donation_list_create'),
    path('donations/edit/<int:pk>/', views.donation_edit, name='donation_edit'),
    path('donations/delete/<int:pk>/', views.donation_delete, name='donation_delete'),
]