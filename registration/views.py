from django.shortcuts import render
from .models import User
from django.template.context_processors import csrf
import re

# Create your views here.
def doreg(request):
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
    msg=''
    #un=User.objects.filter(username=uname,password=passwd)
    if passwd==cpasswd:
        if re.search(regex1,email) and re.search(regex2,mobile):
            user=User.objects.filter(username=uname)
            if user.exists():
                flag=1
                msg='Username is already taken'
        else:
            flag=1
    else:
        flag=1
    if flag==0:
        u=User(username=uname,password=passwd,p_name=p_name,mobile_no=mobile,email_id=email,address=address)
        u.save()
        return render(request,'confirmreg.html',context={'uname':uname,'p_name':p_name,'email':email,'mobile':mobile,'address':address})
    else:
        if msg=='':
            return render(request,'invalidreg.html')
        else:
            return render(request,'invalidreg.html',{'msg':msg})


def regist(request):
    c={}
    c.update(csrf(request))
    return render(request,'registration.html',c)