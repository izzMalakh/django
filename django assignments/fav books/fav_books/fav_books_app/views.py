from django.shortcuts import render,redirect
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
    messages.success(request, "Thank you! account successfully registered", extra_tags="suc")

    user.save()
    
    
    return redirect('/')
    
    
def login(request):
    user = User.objects.filter(email=request.POST['login_email'])
    # the filter brj3 array
    if user: #يعني ازا اليوزر مش فاضي 
        logged_user=user[0]
        if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()): #يعين قارن هاش مع هاش موجود في الداتا بيس
            userr = User.objects.get(email = request.POST['login_email'])
            request.session['id_of_user'] = userr.id
            print(request.session['id_of_user'])
            request.session['firstname_of_user'] = userr.first_name.title()
            return redirect('/books')
        messages.error(request, "wrong email or password", extra_tags="wrong")
        return redirect('/')
    messages.error(request, "wrong email or password", extra_tags="wrong")
    return redirect('/')



def viewBooks(request):
    context={
        'user':User.objects.get(id=request.session['id_of_user']),
        'allbook':Book.objects.all(),

    }
    return render(request, "books.html",context)

def addBook(request):
    errors = Book.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/books')
    user= User.objects.get(id=request.session['id_of_user'])
    book=Book.objects.create(title=request.POST['booTtitle'],desc=request.POST['bookDescription'],uploaded_by=user)
    userid= request.session['id_of_user']
    current_user= User.objects.get(id=userid)
    book.user_who_like.add(current_user)
    book.save()
    return redirect('/books')

def BookDetails(request,id):
    book1=Book.objects.get(id=id)
    # likebook=book1.user_who_like.filter(id=request.session['user_id'])
    context={
        'user':User.objects.get(id=request.session['id_of_user']),
        'book':Book.objects.get(id=id),
        'this':book1.uploaded_by,
        'likes':book1.user_who_like.all(),
        # 'likebook':likebook
    }
    
    return render(request, "showdetails.html",context)

def editdescription(request,id):
    book1=Book.objects.get(id=id)
    if request.POST['button']=='update':
        book1.title= request.POST['titleedit']
        book1.desc= request.POST['editdes']
        book1.save()
        return redirect('/books/'+str(id))
    elif request.POST['button']=='delete':
        book1=Book.objects.get(id=id)
        book1.delete()
        return redirect('/books')


# def deletebook(request,id):
#     book1=Book.objects.get(id=id)
#     book1.delete()
#     return redirect('/books')

def logout(request):
    request.session.delete()
    return redirect('/')

def addToFav(request,id):
    bookid= Book.objects.get(id=id)
    print(bookid.user_who_like)
    userid= request.session['id_of_user']
    bookid= Book.objects.get(id=id)
    current_user= User.objects.get(id=userid)
    print(bookid)
    print(request.session['id_of_user'])
    bookid.user_who_like.add(current_user)
    return redirect('/books')

def addFavButton(request,id):
    userid= request.session['id_of_user']
    bookid= Book.objects.get(id=id)
    current_user= User.objects.get(id=userid)
    bookid.user_who_like.add(current_user)
    return redirect('/books/'+str(id))
def unFav(request,id):
    userid= request.session['id_of_user']
    bookid= Book.objects.get(id=id)
    current_user= User.objects.get(id=userid)
    bookid.user_who_like.remove(current_user)
    #delete ما بتنفع 
    return redirect('/books/'+str(id))

def allfav(request):
    userid= request.session['id_of_user']
    current_user= User.objects.get(id=userid)
    allfav= current_user.liked_books.all()
    context={
        'allfav':allfav,
        'current_user':current_user,
        
    }
    return render(request, "allfavbooks.html",context)