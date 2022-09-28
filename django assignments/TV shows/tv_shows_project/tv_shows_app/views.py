from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
def allshows(request):
    context={
        'allshows':Show.objects.all()
    }
    return render(request, "allshows.html",context)

def AddNewShow(request):
    return render(request,"addshows.html")

def submitshow(request):
    show = Show.objects.create(title=request.POST['titleshow'],network=request.POST['network'],release_date=request.POST['date'],description=request.POST['des'])
    # note: all the variables inside curly brackets are read and replaced by their value
    return redirect(f'/shows/{show.id}')

def ShowDetails(request,id):
    context={
        'show':Show.objects.get(id=int(id))
    }
    return render(request, "showdetails.html",context)
def editpagerender(request,id):
    context={
        'show':Show.objects.get(id=id)
    }
    return render(request, "editshow.html", context)

def editshow(request,id):
    show = Show.objects.get(id=id)
    show.title = request.POST['titleshow']
    show.network = request.POST['network']
    show.release_date = request.POST['date']
    show.description = request.POST['des']
    show.save()
    return redirect("/shows/"+str(id))


def deleteShow(request,id):
    show=Show.objects.get(id=id)
    show.delete()
    return redirect("/")