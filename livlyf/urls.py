from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.About,name='about'),
    path('',views.Home,name='home'),
    path('contact/',views.Contact,name='contact'), 
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handleLogin, name="handleLogin"),
    path('logout/', views.handleLogout, name="handleLogout"),
    path('vaccines/', views.Vaccines, name="vaccines"),
    path('hospitals/', views.Hospitals, name="hospitals"),
    path('centers/', views.Centers, name="centers"),
    path('appointment/', views.Appointment, name="appointment"),
    path('patient/', views.Patients, name="patient"),
    path('profile/', views.Profile, name="profile"),






]
