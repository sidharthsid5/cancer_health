from django.urls import path
from . import views

urlpatterns = [
    # PatHealthRec URLs
    path('pat-health-recs/', views.pat_health_rec_list_create, name='pat_health_rec_list_create'),
    path('pat-health-recs/edit/<int:pk>/', views.pat_health_rec_edit, name='pat_health_rec_edit'),
    path('pat-health-recs/delete/<int:pk>/', views.pat_health_rec_delete, name='pat_health_rec_delete'),

    # ApplyScan URLs
    path('apply-scans/', views.apply_scan_list_create, name='apply_scan_list_create'),
    path('apply-scans/edit/<int:pk>/', views.apply_scan_edit, name='apply_scan_edit'),
    path('apply-scans/delete/<int:pk>/', views.apply_scan_delete, name='apply_scan_delete'),

    # CounsellingBook URLs
    path('counselling-books/', views.counselling_book_list_create, name='counselling_book_list_create'),
    path('counselling-books/edit/<int:pk>/', views.counselling_book_edit, name='counselling_book_edit'),
    path('counselling-books/delete/<int:pk>/', views.counselling_book_delete, name='counselling_book_delete'),

    # RegFreevig URLs
    path('reg-freevigs/', views.reg_freevig_list_create, name='reg_freevig_list_create'),
    path('reg-freevigs/edit/<int:pk>/', views.reg_freevig_edit, name='reg_freevig_edit'),
    path('reg-freevigs/delete/<int:pk>/', views.reg_freevig_delete, name='reg_freevig_delete'),

    # Comments URLs
    path('comments/', views.comments_list_create, name='comments_list_create'),
    path('comments/edit/<int:pk>/', views.comments_edit, name='comments_edit'),
    path('comments/delete/<int:pk>/', views.comments_delete, name='comments_delete'),
]