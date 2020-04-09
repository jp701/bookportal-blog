from django.shortcuts import render
from django.template.context_processors import csrf
from registration.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sessions.models import Session

# Create your views here.
def login(request):
    c={}
    c.update(csrf(request))
    return render(request,'login.html',c)

def home(request):
    if 'username' in request.session:
        uname=request.session['username']
        user=User.objects.get(username=uname)
        return render(request,'loggedin.html',{'user':user})
    else:
        return HttpResponseRedirect('/loginm/login/')

def delsession(request):
    Session.objects.all().delete()
    return HttpResponse('Good job, All sessions deleted!!')


def logout(request):
    if 'username' in request.session:
        Session.objects.all().delete()
        c={}
        c.update(csrf(request))
        msg='You are logged out, Please login again...'
        return render(request,'login.html',{'c':c,'msg':msg})
    else:
        return HttpResponseRedirect('/loginm/login/')

def invalid(request):
    return render(request,'invalidlogin.html')
# render to render to some template and HttpResponseRedirect to redirect the response to other view


def auth_user(request):
    uname=request.POST.get('username','')
    passwd=request.POST.get('password','')
    try:
        user1=User.objects.get(username=uname,password=passwd)
        request.session['username']=uname
        return render(request,'loggedin.html',{'user': user1})
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/loginm/invalid/')

def aboutus(request):
    return render(request,'aboutus.html')
