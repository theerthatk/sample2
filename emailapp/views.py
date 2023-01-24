import uuid

from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
from emailproject.settings import EMAIL_HOST_USER

from.models import *
from django.contrib.auth import messages





# Create your views here.

def register(request):
    a=regform()
    return render(request,'register.html',{'form':a})

def contact(request):
    a=contactform()
    if request.method=='POST':
        b=contactform(request.POST)
        if b.is_valid():
            nm=b.cleaned_data['name']
            em=b.cleaned_data['email']
            ms=b.cleaned_data['message']
            send_mail(str(nm)+"||"+"TCS", ms, EMAIL_HOST_USER, [em])
            return render(request,"success.html")
    #         send_mail(subject,message,EMAIL_HOST_USER,[EMAIL]



    return render(request,'contact.html',{'form':a})

def regis(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(username=username).first():
            messages.success(request,'username already taken')
            return redirect(regis)
        if User.objects.filter(email=email).first():
            messages.success(request, 'email already taken')
            return redirect(regis)

        user_obj=User(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        auth_taken=str(uuid.uuid4())
        profile_obj=profile.objects.create(user=user_obj,auth_token=auth_taken)
        profile_obj.save()
        send_mail_regis(email,auth_taken)
        return render(request,'success.html')

    return render(request,'register1.html')


def send_mail_regis(email,auth_token):
    subject='your account has been verified'
    message=f'paste your link to verify your account  http://127.0.0.1:8000/emailapp/verify/'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

