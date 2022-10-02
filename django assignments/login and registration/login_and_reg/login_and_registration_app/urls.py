from django.urls import path
from . import views

urlpatterns = [
    path('', views.method),
    path('registration', views.registration),
    path('login', views.login),
    
]
