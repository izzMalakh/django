from django.shortcuts import render,HttpResponse

# Create your views here.
def default(request):
    return HttpResponse("Now you in the default page from method in users app ,, Type /blogs in the domain to go to the blogs app, and /surveys to go the surveys app")
def register(request):
    return HttpResponse("placeholder for users to create a new user record")
def login(request):
    return HttpResponse("placeholder for users to log in")
def user(request):
    return HttpResponse("placeholder to later display all the list of users")