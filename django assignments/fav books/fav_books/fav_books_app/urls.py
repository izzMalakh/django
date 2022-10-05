from django.urls import path
from . import views

urlpatterns = [
    path('', views.method),
    path('registration', views.registration),
    path('login', views.login),
    path('books', views.viewBooks),
    path('addbook', views.addBook),
    path('books/<int:id>', views.BookDetails),
    path('editdes/<int:id>', views.editdescription),
    # path('destroybook/<int:id>', views.deletebook),
    path('logout', views.logout),
    path('addtofav/<int:id>', views.addToFav),
    path('addFavButton/<int:id>', views.addFavButton),
    path('unFavButton/<int:id>', views.unFav),
    path('allfav', views.allfav),

    
]
