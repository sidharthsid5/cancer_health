from django.urls import path
from . import views

urlpatterns = [
    # CancerType URLs
    path('cancer-types/', views.cancer_type_list_create, name='cancer_type_list_create'),
    path('cancer-types/edit/<int:pk>/', views.cancer_type_edit, name='cancer_type_edit'),
    path('cancer-types/delete/<int:pk>/', views.cancer_type_delete, name='cancer_type_delete'),

    # ScanType URLs
    path('scan-types/', views.scan_type_list_create, name='scan_type_list_create'),
    path('scan-types/edit/<int:pk>/', views.scan_type_edit, name='scan_type_edit'),
    path('scan-types/delete/<int:pk>/', views.scan_type_delete, name='scan_type_delete'),

    # ScanCenter URLs
    path('scan-centers/', views.scan_center_list_create, name='scan_center_list_create'),
    path('scan-centers/edit/<int:pk>/', views.scan_center_edit, name='scan_center_edit'),
    path('scan-centers/delete/<int:pk>/', views.scan_center_delete, name='scan_center_delete'),

    # CounCenter URLs
    path('coun-centers/', views.coun_center_list_create, name='coun_center_list_create'),
    path('coun-centers/edit/<int:pk>/', views.coun_center_edit, name='coun_center_edit'),
    path('coun-centers/delete/<int:pk>/', views.coun_center_delete, name='coun_center_delete'),

    # HairDonCriteria URLs
    path('hair-don-criteria/', views.hair_don_criteria_list_create, name='hair_don_criteria_list_create'),
    path('hair-don-criteria/edit/<int:pk>/', views.hair_don_criteria_edit, name='hair_don_criteria_edit'),
    path('hair-don-criteria/delete/<int:pk>/', views.hair_don_criteria_delete, name='hair_don_criteria_delete'),

    # MedServices URLs
    path('med-services/', views.med_services_list_create, name='med_services_list_create'),
    path('med-services/edit/<int:pk>/', views.med_services_edit, name='med_services_edit'),
    path('med-services/delete/<int:pk>/', views.med_services_delete, name='med_services_delete'),

    # GuideLines URLs
    path('guide-lines/', views.guide_lines_list_create, name='guide_lines_list_create'),
    path('guide-lines/edit/<int:pk>/', views.guide_lines_edit, name='guide_lines_edit'),
    path('guide-lines/delete/<int:pk>/', views.guide_lines_delete, name='guide_lines_delete'),

    # DietaryTip URLs
    path('dietary-tips/', views.dietary_tip_list_create, name='dietary_tip_list_create'),
    path('dietary-tips/edit/<int:pk>/', views.dietary_tip_edit, name='dietary_tip_edit'),
    path('dietary-tips/delete/<int:pk>/', views.dietary_tip_delete, name='dietary_tip_delete'),

    # DietarySupply URLs
    path('dietary-supplies/', views.dietary_supply_list_create, name='dietary_supply_list_create'),
    path('dietary-supplies/edit/<int:pk>/', views.dietary_supply_edit, name='dietary_supply_edit'),
    path('dietary-supplies/delete/<int:pk>/', views.dietary_supply_delete, name='dietary_supply_delete'),

    # Events URLs
    path('events/', views.events_list_create, name='events_list_create'),
    path('events/edit/<int:pk>/', views.events_edit, name='events_edit'),
    path('events/delete/<int:pk>/', views.events_delete, name='events_delete'),

    # Admin URLs
    path('admins/', views.admin_list_create, name='admin_list_create'),
    path('admins/edit/<str:pk>/', views.admin_edit, name='admin_edit'), #pk is string because username is primary key
    path('admins/delete/<str:pk>/', views.admin_delete, name='admin_delete'),

    # State URLs
    path('states/', views.state_list_create, name='state_list_create'),
    path('states/edit/<int:pk>/', views.state_edit, name='state_edit'),
    path('states/delete/<int:pk>/', views.state_delete, name='state_delete'),

    # Dist URLs
    path('dists/', views.dist_list_create, name='dist_list_create'),
    path('dists/edit/<int:pk>/', views.dist_edit, name='dist_edit'),
    path('dists/delete/<int:pk>/', views.dist_delete, name='dist_delete'),
]