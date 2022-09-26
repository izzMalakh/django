from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.
def method(request):
    context = { 
        "Dojos":Dojo.objects.all()
    }
    if 'count' and 'countt'  not in request.session:
            request.session['count']= 0
            request.session['countt']= 0
            

    
    return render(request, "dojo_ninjas.html",context)

def index1(request):
    Dojo.objects.create(name=request.POST['name'],city=request.POST['city'],state=request.POST['state'])
    request.session['count']+=1
    
    return redirect("/")


def index2(request):
    dojox=Dojo.objects.get(id=request.POST['selectdojo'])
    Ninja.objects.create(first_name=request.POST['firstname'],last_name=request.POST['lastname'],dojo=dojox)
    request.session['countt']+=1
    return redirect("/")

def destroy(request):
    if request.POST['reset'] == 'rn':
        alldojos = Ninja.objects.all()
        alldojos.delete()
        request.session['countt']= 0
    elif request.POST['reset'] == 'rd':
        
        request.session['count']=1
        alldojos2 = Dojo.objects.all()
        alldojos2.delete()
        request.session['count']= 0
        request.session['countt']= 0
        
    
    return redirect("/")
    
    
