from django.urls import path
from . import views

urlpatterns = [
    path('', views.method),
    path('/new', views.new),
   
]