from django.urls import path
from . import views

urlpatterns = [
    path('', views.allshows),
    path('addnewShow', views.AddNewShow),
    path('shows', views.submitshow),
    path('shows/<id>', views.ShowDetails),
    path('edit/<id>', views.editpagerender),
    path('editshow/<id>', views.editshow),
    path('destroy/<id>', views.deleteShow),
]
