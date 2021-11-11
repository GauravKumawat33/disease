from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.About,name='about'),
    path('',views.Home,name='home'),
    path('contact/',views.Contact,name='contact'), 
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handleLogin, name="handleLogin"),
    path('logout/', views.handleLogout, name="handleLogout"),

]
