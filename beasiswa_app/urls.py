from django.urls import path
from . import views

app_name = 'beasiswa_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('beasiswa-list/', views.beasiswa_list, name='beasiswa_list'),
    path('apply-beasiswa/', views.apply_beasiswa, name='apply_beasiswa'),
    path('status-beasiswa/', views.status_beasiswa, name='status_beasiswa'),
    path('mahasiswa/profile/', views.profile, name='mahasiswa_profile'),
    path('manage-beasiswa/', views.manage_beasiswa, name='manage_beasiswa'),
    path('manage-mahasiswa/', views.manage_mahasiswa, name='manage_mahasiswa'),
    path('message-list/', views.message_list, name='message_list'),
    path('login/', views.mahasiswa_login, name='login'),
    path('register/', views.mahasiswa_register, name='register'),
    path('logout/', views.mahasiswa_logout, name='logout'),   
]
