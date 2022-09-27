from django.urls import path
from . import views

urlpatterns = [
    path('', views.addbookpage),
    path('addbook', views.addbook),
    path('viewbook/<id>', views.viewbook),
    path('addauthor/<id>', views.addauthortobook),

    path('authors/', views.addauthorpage),
    path('addauthor', views.addauthor),
    path('viewauthor/<id>', views.viewauthor),
    path('addbooks/<id>', views.addbooktoauthor),
    path('reset', views.reset),



    
    
    

]
