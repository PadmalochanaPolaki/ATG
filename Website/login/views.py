from django.shortcuts import *
from .models import *
# Create your views here.

def home(request):
    return render(request,"index.html")


def login(request):
        return render(request,"login.html")


def signup(request):
        return render(request,"signup.html")

def addblog(request):
        return render(request,"addblog.html")

def viewblog(request):
        return render(request,"viewblog.html")





def signupaction(request):
     if request.method == "POST":
        Fname=request.POST["fname"]
        Lname=request.POST["lname"]
        Username=request.POST["user"]
        email=request.POST["mail"]
        password=request.POST["pass"]
        address=request.POST["add"]

        d=data(Fname=Fname, Lname=Lname, Username=Username,email=email,password=password,Address=address)
        d.save()
        msg2='Your account created succesfully, you can login'
        return render(request, 'login.html', {'msg2':msg2})  
     

from django.shortcuts import render, redirect

def loginaction(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('pwd')

        if username == 'Patient' and password == 'Patient':
            # Redirect to patient dashboard or any specific page for patients
            return render(request, 'patient.html')
        elif username == 'Doctor' and password == 'Doctor':
            # Redirect to doctor dashboard or any specific page for doctors
            return render(request, 'doctor.html')
        else:
            msg = 'Login Failed. Invalid username or password.'
            return render(request, 'login.html', {'msg': msg})

    return render(request, 'login.html')