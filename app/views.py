from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.

def RegisterPage(request):
    return render(request,"app/register.html")

#view for user registaion

def UserRegister(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        
        #Fisrt we will validate that user already exist
        user=User.objects.filter(Email=email)
        
        if user:
            message="User already exist"
            return render(request,"app/Login.html",{'msg':message})
        else:
            if password==cpassword:
                newuser=User.objects.create(Firstname=fname,Lasttname=lname,Email=email,Contact=contact,Password=password)
              
                
                message="User register Sucessfully"
                
                return render(request,"app/login.html",{'msg':message})
            
            else:
                message ="Password and conform Password Doesnot match"
                return render(request,"app/register.html",{'msg':message})
            
            