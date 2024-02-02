from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('login/', views.view_login, name='login'),
    path('register-user/', views.register, name='register-user'),
    path('krijo-orar/', views.create_timetable, name='krijo-orar'),
    path('lista-e-orarit/', views.timetable_list, name='lista-e-orarit'),
    # path('get_options/', views.get_options, name='get_options'),
]