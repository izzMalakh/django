from django.urls import path
from . import views

urlpatterns = [
    path('', views.method),
    path('process1',views.index1),
    path('process2',views.index2),
    path('reset',views.destroy),
]
