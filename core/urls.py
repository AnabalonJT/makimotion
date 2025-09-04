from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Patient URLs
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/<int:pk>/edit/', views.patient_update, name='patient_update'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    
    # Appointment URLs
    path('patients/<int:patient_id>/appointments/add/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointments/<int:pk>/edit/', views.appointment_update, name='appointment_update'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
    
    # Clinical Records (Fichas Clínicas) URLs
    path('patients/<int:patient_pk>/fichas-clinicas/', views.ficha_clinica_list, name='ficha_clinica_list'),
    path('patients/<int:patient_pk>/fichas-clinicas/add/', views.ficha_clinica_create, name='ficha_clinica_create'),
    path('patients/<int:patient_pk>/fichas-clinicas/<int:pk>/', views.ficha_clinica_detail, name='ficha_clinica_detail'),
    path('patients/<int:patient_pk>/fichas-clinicas/<int:pk>/edit/', views.ficha_clinica_update, name='ficha_clinica_update'),
    path('patients/<int:patient_pk>/fichas-clinicas/<int:pk>/delete/', views.ficha_clinica_delete, name='ficha_clinica_delete'),
]