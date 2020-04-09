from django.shortcuts import render
from django.template.context_processors import csrf
from registration.models import User,AvailBooks
from django.http import HttpResponseRedirect

# Create your views here.
def upload(request):
    if 'username' in request.session:
        c={}
        c.update(csrf(request))
        return render(request,'uploadbook.html',c)
    else:
        return HttpResponseRedirect('/loginm/login/')

def uploadeddetails(request):
    c={}
    c.update(csrf(request))
    if 'username' in request.session:    
        name=request.POST.get('bname','')
        isbn=request.POST.get('bisbn','')
        author=request.POST.get('author','')
        publisher=request.POST.get('pub','')
        price=request.POST.get('price','')
        desc=request.POST.get('des','')
        category=request.POST.get('category','')
        image=request.FILES['img']

        uname=request.session['username']
        user=User.objects.get(username=uname)
        img=AvailBooks(b_ISBN=isbn,b_name=name,b_author=author,b_price=price,b_publisher=publisher,b_description=desc,b_category=category,uploader_name=user,b_photo=image)
        img.save()
        return render(request,'uploadeddetails.html',{'c':c,"img":img})
    else:
        return HttpResponseRedirect('/loginm/login/')
        
def getdetails(request):
    c={}
    c.update(csrf(request))
    value=request.POST.get('update','')
    if 'username' in request.session:
        bname=request.POST.get('hidden','')
        uname=request.session['username']
        user=User.objects.get(username=uname)
        if value=='Update' or value=='Update details':
            book=AvailBooks.objects.get(b_name=bname,uploader_name_id=user)
            return render(request,'updatedetails.html',{'c':c,'book':book})
        elif value=='Delete':
            AvailBooks.objects.filter(b_name=bname,uploader_name_id=user).delete()
            return HttpResponseRedirect('/profile/uploaded/')
    else:
        return HttpResponseRedirect('/loginm/login/')

def updatedetails(request):
    if 'username' in request.session:
        name=request.POST.get('bname','')
        isbn=request.POST.get('bisbn','')
        author=request.POST.get('author','')
        publisher=request.POST.get('pub','')
        price=request.POST.get('price','')
        desc=request.POST.get('des','')
        category=request.POST.get('cate','')
        if 'username' in request.session:
            uname=request.session['username']
        user=User.objects.get(username=uname)
        hidden=request.POST.get('hidden','')
        book=AvailBooks.objects.filter(b_name=hidden,uploader_name_id=user)
        filepath=request.FILES.get('img',False)
        if filepath:
            image=request.FILES['img']
        else:
            image=book[:1].get().b_photo
        user=User.objects.get(username=uname)
        book.update(b_ISBN=isbn,b_name=name,b_author=author,b_price=price,b_publisher=publisher,b_description=desc,b_category=category,uploader_name=user,b_photo=image)
        img=AvailBooks.objects.get(b_name=name,uploader_name_id=user)
        return render(request,'updatedetails.html',{'img':img})
    else:
        return HttpResponseRedirect('/loginm/login/')
