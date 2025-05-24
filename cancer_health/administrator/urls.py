from django.urls import path
from . import views

urlpatterns = [

    # View Counselling booking
    path('admin_counselling_appointments/', views.admin_counselling_appointments, name='admin_counselling_appointments'),

    # View appointments
    path('admin_view_appointments/', views.admin_view_appointments, name='admin_view_appointments'),

    # View Health Records
    path('admin_health_records/', views.admin_health_records, name='admin_health_records'),

    # Home
    path('', views.homes, name='homes'),

    # CancerType URLs
    path('cancer_type_list_create/', views.cancer_type_list_create, name='cancer_type_list_create'),
    path('cancer_type_list_create<int:pk>/', views.cancer_type_edit, name='cancer_type_edit'),
    path('cancer_type_delete/<int:pk>/', views.cancer_type_delete, name='cancer_type_delete'),

    # ScanType URLs
    path('scan_type_list_create/', views.scan_type_list_create, name='scan_type_list_create'),
    path('scan_type_edit/<int:pk>/', views.scan_type_edit, name='scan_type_edit'),
    path('scan_type_delete/<int:pk>/', views.scan_type_delete, name='scan_type_delete'),

    # ScanCenter URLs
    path('scan_center_list_create/', views.scan_center_list_create, name='scan_center_list_create'),
    path('scan_center_edit<int:pk>/', views.scan_center_edit, name='scan_center_edit'),
    path('scan_center_delete/<int:pk>/', views.scan_center_delete, name='scan_center_delete'),

    # CounCenter URLs
    path('coun_center_list_create/', views.coun_center_list_create, name='coun_center_list_create'),
    path('coun_center_edit/<int:pk>/', views.coun_center_edit, name='coun_center_edit'),
    path('coun_center_delete/<int:pk>/', views.coun_center_delete, name='coun_center_delete'),

    # HairDonCriteria URLs
    path('hair_don_criteria_list_create/', views.hair_don_criteria_list_create, name='hair_don_criteria_list_create'),
    path('hair_don_criteria_edit/<int:pk>/', views.hair_don_criteria_edit, name='hair_don_criteria_edit'),
    path('hair_don_criteria_delete/<int:pk>/', views.hair_don_criteria_delete, name='hair_don_criteria_delete'),

    # MedServices URLs
    path('med_services_list_create/', views.med_services_list_create, name='med_services_list_create'),
    path('med_services_edit/<int:pk>/', views.med_services_edit, name='med_services_edit'),
    path('med_services_delete/<int:pk>/', views.med_services_delete, name='med_services_delete'),

    # GuideLines URLs
    path('guide_lines_list_create/', views.guide_lines_list_create, name='guide_lines_list_create'),
    path('guide_lines_edit/<int:pk>/', views.guide_lines_edit, name='guide_lines_edit'),
    path('guide_lines_delete/<int:pk>/', views.guide_lines_delete, name='guide_lines_delete'),

    # DietaryTip URLs
    path('dietary_tip_list_create/', views.dietary_tip_list_create, name='dietary_tip_list_create'),
    path('dietary_tip_edit/<int:pk>/', views.dietary_tip_edit, name='dietary_tip_edit'),
    path('dietary_tip_delete/<int:pk>/', views.dietary_tip_delete, name='dietary_tip_delete'),

    # DietarySupply URLs
    path('dietary_supply_list_create/', views.dietary_supply_list_create, name='dietary_supply_list_create'),
    path('dietary_supply_edit/<int:pk>/', views.dietary_supply_edit, name='dietary_supply_edit'),
    path('dietary_supply_delete/<int:pk>/', views.dietary_supply_delete, name='dietary_supply_delete'),

    # Events URLs
    path('events_list_create/', views.events_list_create, name='events_list_create'),
    path('events_edit/<int:pk>/', views.events_edit, name='events_edit'),
    path('events_delete/<int:pk>/', views.events_delete, name='events_delete'),

    # State URLs
    path('state_list_create/', views.state_list_create, name='state_list_create'),
    path('state_edit/<int:pk>/', views.state_edit, name='state_edit'),
    path('state_delete/<int:pk>/', views.state_delete, name='state_delete'),

    # Dist URLs
    path('dist_list_create/', views.dist_list_create, name='dist_list_create'),
    path('dist_edit/<int:pk>/', views.dist_edit, name='dist_edit'),
    path('dist_delete/<int:pk>/', views.dist_delete, name='dist_delete'),
]