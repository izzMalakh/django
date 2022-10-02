import email
from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
import bcrypt

def method(request):
    return render(request, "home.html")

def registration(request):
    errors = User.objects.basic_validator(request.POST)
    

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            print(errors)
        return redirect('/')
    fname= request.POST["fname"]
    lname= request.POST["lname"]
    email= request.POST["email"]
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(first_name=fname , last_name=lname, email=email, password=pw_hash)
    # request.session['fname']=User.objects.last().first_name
    user.save()
    messages.success(request, "Thank you! account successfully registered", extra_tags="suc")
    
    return redirect('/')
    
    
def login(request):
    user = User.objects.filter(email=request.POST['login_email'])
    # the filter brj3 array
    if user: #يعني ازا اليوزر مش فاضي 
        logged_user=user[0]
        if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()): #يعين قارن هاش مع هاش موجود في الداتا بيس
            context={
                'obj':User.objects.last()
            }
            
            return render(request, "sucess.html",context)
        messages.error(request, "wrong email or password", extra_tags="wrong")
        return redirect('/')
    messages.error(request, "wrong email or password", extra_tags="wrong")
    return redirect('/')

    