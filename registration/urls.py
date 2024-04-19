from django.urls import path
from . import views

urlpatterns = [
    path('registration/',views.registration, name='registration'),
    path('enrollmypage/',views.mypage, name='myregisterpage'),

    path('home',views.home, name='myhome'),
    path('login/',views.login, name='myloginpage'),
    path('courses/',views.courses, name='coursespage'),

    path('addstudent',views.dashboard, name='addstudent'),
    path('',views.dashboard, name='dashboardpage'),
    path('addstudent',views.addstudent, name='addstudent'),


]







