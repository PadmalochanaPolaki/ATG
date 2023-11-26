from django.shortcuts import *
from .models import *
# Create your views here.

def home(request):
    return render(request,"index.html")


def login(request):
        return render(request,"login.html")


def signup(request):
        return render(request,"signup.html")




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
     

def loginaction(request):
    uid=request.POST['Username']
    pwd=request.POST['pwd']
    d=data.objects.filter(Username__exact=uid).filter(password__exact=pwd).count()
    if d>0:
        return render(request, 'patient.html')
    else:
        msg1='Login Fail'

        return render(request, 'login.html', {'msg':msg1})
    

