from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('/user_registration' , views.user_registration , name="user_registration"),
    path('/user_login' , views.login , name="login"),
    path('/user_logout' , views.logout , name="logout"),

]