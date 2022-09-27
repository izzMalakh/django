from multiprocessing import context
from re import X
from django.shortcuts import render,redirect

from books_authors_app.models import *

def addbookpage(request):
    context={
        'allbooks':Book.objects.all()
    }
    return  render(request, "addbooks_page.html",context)

def addbook(request):
    Book.objects.create(title=request.POST['titleinput'],description=request.POST['desinput'])
    return redirect ("/")

def viewbook(request,id):
    book1= Book.objects.get(id=int(id))
    context={
        'book':Book.objects.get(id=int(id)),
        'allauthors':Author.objects.all(),
        'var':book1.authors.all()

    }
    return render(request, "viewbooks.html",context)

def addauthortobook(request,id):
    book1= Book.objects.get(id=int(id))
    author1= Author.objects.get(id=request.POST['selectauthors'])
    book1.authors.add(author1)

    return redirect("/viewbook/"+str(id))


def addauthorpage(request):
    context={
        'allauthors':Author.objects.all()
    }
    return  render(request, "addauthor_page.html",context)

def addauthor(request):
    Author.objects.create(first_name=request.POST['firstnameinput'],last_name=request.POST['lastnameinput'],notes=request.POST['notes'])
    return redirect ("/authors")

def viewauthor(request,id):
    author1= Author.objects.get(id=int(id))
    
    context={
        'author':Author.objects.get(id=int(id)),
        'allbooks':Book.objects.all(),
        'var':author1.books.all()

    }
    return render(request, "viewauthor.html",context)
def addbooktoauthor(request,id):
    
    author1= Author.objects.get(id=int(id))
    book1= Book.objects.get(id=request.POST['selectbooks'])
    author1.books.add(book1)
    

    return redirect("/viewauthor/"+str(id))

def reset(request):
    allauthors=Author.objects.all()
    allauthors.delete()
    return render(request, "addauthor_page.html")
    
    
    




