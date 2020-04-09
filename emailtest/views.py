from django.shortcuts import render
from django.conf import settings
from django.template.context_processors import csrf
from registration.models import User
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
user= None

def forgotpass(request):
    c={}
    c.update(csrf(request))
    return render(request,'forgotpassword1.html',c)

"""
import random,string to generate random password
def randomPass(len=8):
    newpass=string.ascii_letters+ string.digits
    return ''.join(random.choice(newpass) for i in range(len))"""
    
def testit(request):
    uname=request.POST.get('username','')
    email=request.POST.get('email','')
    global user
    user=User.objects.filter(username=uname,email_id=email)
    if user.exists():
        user=user[:1].get()
        subject='forgot password'
        email_from=settings.EMAIL_HOST_USER
        email_to=user.email_id
        content='Click below link to reset your password\n'+'http://mjbookportal.pythonanywhere.com/email/gotoresetlink/'
        list=[]
        list.append(email_to)
        send_mail(subject,content,email_from,list)
        return render(request,'forgotpassword1.html',{'check':'We have e-mailed your password reset link'})
    else:
        return render(request,'forgotpassword1.html',{'msg':'Account doesn\'t exists, try another username or password'})


def gotoresetlink(request):
    c={}
    c.update(csrf(request))
    global user
    return render(request,'resetpassword1.html',{'c':c,'user':user})

def resetpassword(request):
    c={}
    c.update(csrf(request))
    uname=request.POST.get('username','')
    password=request.POST.get('password','')
    cpasswd=request.POST.get('cpassword','')
    if password==cpasswd:
        getuser=User.objects.filter(username=uname)
        getuser.update(username=uname,password=password)
        user1=User.objects.get(username=uname,password=password)
        return render(request,'resetpassword1.html',{'c':c,'user1':user1})
    else:
        global user
        return render(request,'resetpassword1.html',{'c':c,'msg':'Password doesnot match, Try again','user':user})
