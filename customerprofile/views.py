from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from registration.models import User,AvailBooks,SoldBooks
import re

# Create your views here.
def profile(request):
    if 'username' in request.session:
        uname=request.session['username']
        try:
            user=User.objects.get(username=uname)
        except User.DoesNotExist:
            user=None
        return render(request,'profile.html',{'user1':user})
    else:
        return HttpResponseRedirect('/loginm/login/')

def editprofile(request):
    if 'username' in request.session:
        c={}
        c.update(csrf(request))
        uname=request.session['username']
        user=User.objects.get(username=uname)
        return render(request,'editprofile.html',{'c':c,'user':user})
    else:
        return HttpResponseRedirect('/loginm/login/')

def updateprofile(request):
    if 'username' in request.session:
        flag=0
        uname=request.POST.get('username','')
        passwd=request.POST.get('password','')
        cpasswd=request.POST.get('cpassword','')
        p_name=request.POST.get('pname','')
        email= request.POST.get('email','')
        mobile=request.POST.get('mob','')
        address=request.POST.get('add','')
        regex1 =r'^\w+@\w+\.(com|ac.in|org)$'
        regex2 =r'^(|\+\d{2}[ -]?)\d{10}$'
        if passwd==cpasswd:
            if re.search(regex1,email) and re.search(regex2,mobile):
                pass
            else:
                flag=1
        else:
            flag=1
        if flag==0:
            user=User.objects.filter(username=uname)
            user.update(username=uname,password=passwd,p_name=p_name,mobile_no=mobile,email_id=email,address=address)
            u=User.objects.get(username=uname)
            request.session['username']=uname
            return render(request,'editprofile.html',context={'user1':u})
        else:
            return render(request,'editprofile.html',{'msg':'Please enter correct registration details..'})
    else:
        return HttpResponseRedirect('/loginm/login/')

def deleteprofile(request):
    if 'username' in request.session:
        uname=request.session['username']
        msg='Your account has been deleted'
        User.objects.get(username=uname).delete()
        return render(request,'deletedetails.html',{'uname':uname,'msg':msg})
    else:
        return HttpResponseRedirect('/loginm/login/')

def uploaded(request):
    if 'username' in request.session:
        c={}
        c.update(csrf(request))
        uname=request.session['username']
        user=User.objects.get(username=uname)
        bk1=AvailBooks.objects.filter(uploader_name_id=user)
        bk2=SoldBooks.objects.filter(seller_name=uname)
        bklist=[]
        for i in bk1:
            bklist.append(i)
        for i in bk2:
            bklist.append(i)
        return render(request,'uploaded.html',{'c':c,'book':bklist})
    else:
        return HttpResponseRedirect('/loginm/login/')

def bought(request):
    if 'username' in request.session:
        uname=request.session['username']
        bk=SoldBooks.objects.filter(buyer_name=uname)
        return render(request,'bought.html',{'book':bk})
    else:
        return HttpResponseRedirect('/loginm/login/')

def sold(request):
    if 'username' in request.session:
        uname=request.session['username']
        bk=SoldBooks.objects.filter(seller_name=uname)
        return render(request,'sold.html',{'book':bk})
    else:
        return HttpResponseRedirect('/loginm/login/')


def deleteall(request):
    if 'username' in request.session:
        uname=request.session['username']
        user=User.objects.get(username=uname)
        AvailBooks.objects.filter(uploader_name=user).delete()
        return HttpResponseRedirect('/loginm/home')
    else:
        return HttpResponseRedirect('/loginm/login/')