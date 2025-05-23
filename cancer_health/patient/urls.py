from django.urls import path
from . import views


urlpatterns = [

    #Home
    path('', views.homee, name='homee'),

    #View Hair donation Criteria
    path('hair_donation_view/', views.hair_donation_view, name='hair_donation_view'),

    # View Medical Services
    path('medical_service_view/', views.medical_service_view, name='medical_service_view'),

    # View Dietary Supplements
    path('dietary_supply_view/',views.dietary_supply_view,name='dietary_supply_view'),

    # View Dietary Tips
    path('dietary_tips_view/', views.dietary_tips_view, name='dietary_tips_view'),


    # View Events
    path('events_patient_view/', views.events_patient_view, name='events_patient_view'),

    #View Guidelines
    path('guidelines_patient_view/', views.guidelines_patient_view, name='guidelines_patient_view'),

    #search Scan center
    path('search_scan_center/', views.search_scan_center, name='search_scan_center'),
    path('getAppointment/', views.getAppointment, name='getAppointment'),

    # Scanlist view
    path('scan_type_view/<scnid>/', views.scan_type_view, name='scan_type_view'),

    # PatHealthRec URLs
    path('pat_health_rec_list_create/', views.pat_health_rec_list_create, name='pat_health_rec_list_create'),
    path('pat_health_rec_edit/<int:pk>/', views.pat_health_rec_edit, name='pat_health_rec_edit'),
    path('pat_health_rec_delete/<int:pk>/', views.pat_health_rec_delete, name='pat_health_rec_delete'),

    # ApplyScan URLs
    path('apply_scan_list_create/', views.apply_scan_list_create, name='apply_scan_list_create'),
    path('apply_scan_edit/<int:pk>/', views.apply_scan_edit, name='apply_scan_edit'),
    path('apply_scan_delete/<int:pk>/', views.apply_scan_delete, name='apply_scan_delete'),

    # CounsellingBook URLs
    path('counselling_book_list_create/', views.counselling_book_list_create, name='counselling_book_list_create'),
    path('counselling_book_edit/<int:pk>/', views.counselling_book_edit, name='counselling_book_edit'),
    path('counselling_book_delete/<int:pk>/', views.counselling_book_delete, name='counselling_book_delete'),

    # RegFreevig URLs
    path('reg_freevig_list_create/', views.reg_freevig_list_create, name='reg_freevig_list_create'),
    path('reg_freevig_edit/<int:pk>/', views.reg_freevig_edit, name='reg_freevig_edit'),
    path('reg_freevig_delete/<int:pk>/', views.reg_freevig_delete, name='reg_freevig_delete'),

    # Comments URLs
    path('comments_list_create/', views.comments_list_create, name='comments_list_create'),
    path('comments_edit/<int:pk>/', views.comments_edit, name='comments_edit'),
    path('comments_delete/<int:pk>/', views.comments_delete, name='comments_delete'),
]