from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index),
    path('/new', views.new),
    path('/creat', views.creat),
    path('/<number>', views.show),
    path('/<number>/edit', views.edit),
    path('/<number>/delete', views.destroy)

]