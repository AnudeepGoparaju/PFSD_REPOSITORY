from django.shortcuts import *
from .forms import *
from django.conf import settings
from django.contrib.auth.models import User,auth
from django.contrib.auth import login
import re
from .models import users
import random,math
from django.core.mail import send_mail
# Create your views here.
def Home(request):
    return render(request,'home.html')
def Login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        user=users.objects.filter(email=email,password=password).values()
        print(user)
        if user:
            request.session['na']=email
            return render(request,'home1.html',{})
        else:
            return render(request,'login.html',{'mess':'Invalid Credentials'})
    return render(request,'login.html',{})
def Register(request):

    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        age = int(request.POST.get('age'))
        print(age)
        balance =int(request.POST.get('balance'))
        xx=users.objects.filter(email=email).values()
        print(email)
        print(xx)
        if xx:
            return render(request, "Register.html", {"mess": "Email Already Exists. Please Login"})
        else:
            res = name != '' and all(chr.isalpha() or chr.isspace() for chr in name)
            if str(res)!="True":
                return render(request,"Register.html",{"mess":"Invalid Input. Only Alphabets"})
            elif((age)<10 or (age)>100):
                return render(request, "Register.html", {"mess":"Age should be in between 10 and 100 to register"})
            elif(balance<0):
                return render(request,"Register.html",{"mess":"Balance should not be negative"})
            form=MemberForm(request.POST or None)
            if form.is_valid:
                form.save()
            return render(request,'login.html',{})
    else:
        return render(request,'register.html',{})

def Navbar(request):
    return  render(request,"Navbar.html")

def Navbar1(request):
    return render(request,"Navbar1.html")

def Home1(request):
    return render(request,"home1.html")

def deposit(request):
    return render(request,"deposit.html")

def depositsuccess(request):
    return render(request,"depositsuccess.html")

def contact(request):
    return render(request,"contact.html")

def credit(request):
    return render(request,"credit.html")

def products(request):
    return render(request,"products.html")

def profile(request):
    x=request.session['na']
    print(x)
    return render(request,"profile.html",{"x":x})

def fedb(request):
    x=request.POST.get('feedback')
    rx=feed.objects.create()
    rx.feedb=x
    rx.save()
    return render(request,"feedback.html")

def resp(request):
    return HttpResponse("We'll respond soon")
def forgot(request):
    return render(request,"forgot.html")
def forgotsent(request):
    global k
    x=request.POST['email']
    request.session["name1"]=x
    k=int(generateOTP())
    print(k)
    subject = 'welcome to Banking Portal'
    message = 'Hi, thank you for registering in Banking Portal.Your otp is '+str(k)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [x, ]
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    return render(request,"forgotsent.html")
def forgotpassword(request):
    global k
    if(request.method=='POST'):
        x=int(request.POST.get("otp"));
        print(x,k)
        if x==k:
            return render(request,"newpass.html")
        else:
            return render(request, "forgotsent.html",{"mess":"OTP WRONG"})
    return render(request,"forgotsent.html")
def newpassword(request):
    y=request.POST["password"]
    z=request.POST["cpassword"]
    q=User.objects.filter(email=request.session['name1']).values()
    if q is not None and y==z:
        cc=users.objects.get(email=request.session['name1'])
        cc.password=y
        cc.save()
        return render(request,"login.html",{"mess":"Sucessfully updated"})
    else:
        return render(request, "newpass.html", {"mess": "Sucessfully Not updated"})
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP