from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeee, name='homeee'),
    # Guest URLs

    path('guest_edit/<int:pk>/', views.guest_edit, name='guest_edit'),
    path('guest_delete/<int:pk>/', views.guest_delete, name='guest_delete'),

    # HairDonation URLs
    path('hair_donation_list_create/', views.hair_donation_list_create, name='hair_donation_list_create'),
    path('hair_donation_edit/<int:pk>/', views.hair_donation_edit, name='hair_donation_edit'),
    path('hair_donation_delete/<int:pk>/', views.hair_donation_delete, name='hair_donation_delete'),

    # Donation URLs
    path('donation_list_create/', views.donation_list_create, name='donation_list_create'),
    path('donation_edit/<int:pk>/', views.donation_edit, name='donation_edit'),
    path('donation_delete/<int:pk>/', views.donation_delete, name='donation_delete'),
]