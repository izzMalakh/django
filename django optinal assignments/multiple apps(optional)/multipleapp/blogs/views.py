from tkinter import N
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def firstpage(request):
    return HttpResponse("you can use this domains: /blogs,/blogs/number,/blogs/new, /blogs/creat ----------- and /surveys to go to second app  surveys app -------- and users to go to third app (user app)")
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def creat(request):
    return redirect('/blogs')

def show(request,number):
    return HttpResponse("placeholder to display blog number:" + str(number) +  " ----------------  " + "write /bolgs/number/edit to edit the number")
    

def edit(request,number):
    return HttpResponse("placeholder to display blog number:" + str(number) + " ----------------  " + "write /bolgs/number/delete to back ")


def destroy(request,number):
    return redirect('/blogs')