from django.shortcuts import render
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from registration.models import User,AvailBooks,SoldBooks
from django.conf import settings

# Create your views here
list=[]

def buy(request):
    if 'username' in request.session:
        c={}
        c.update(csrf(request))
        return render(request,'buybook.html',{'c':c,'STATIC_URL':settings.STATIC_URL})
    else:
        return HttpResponseRedirect('/loginm/login/')

def getcategory(request):
    if 'username' in request.session:
        c={}
        c.update(csrf(request))
        category=request.POST.get('category','')
        user=User.objects.get(username=request.session['username'])
        book=AvailBooks.objects.filter(b_category=category).exclude(uploader_name_id=user)
        if book.exists(): 
            pass
        else:
            book='notfound'
        return render(request,'showbycategory.html',{'c':c,'book':book})
    else:
        return HttpResponseRedirect('/loginm/login/')

def search(request):
    if 'username' in request.session:
        c={}
        c.update(csrf(request))
        searchby=request.POST.get('searchby','')
        sort=request.POST.get('sort','')
        value=request.POST.get('search','')
        msg=''
        if searchby!='select' and value:
            user=User.objects.get(username=request.session['username'])
            if searchby=='b_ISBN':
                book=AvailBooks.objects.filter(b_ISBN=value).exclude(uploader_name_id=user)
            elif searchby=='b_name':
                book=AvailBooks.objects.filter(b_name=value).exclude(uploader_name_id=user)
            elif searchby=='b_author':
                book=AvailBooks.objects.filter(b_author=value).exclude(uploader_name_id=user)
            elif searchby=='b_publisher':
                book=AvailBooks.objects.filter(b_publisher=value).exclude(uploader_name_id=user)
            elif searchby=='seller_name':
                user1=User.objects.get(username=value)
                book=AvailBooks.objects.filter(uploader_name_id=user1).exclude(uploader_name_id=user)
            else:
                book='notfound'
            if book!='notfound' and book.exists():
                if book.count()==1:
                    book[:1].get()
            else:
                msg='No items matched'
        elif sort!='select1':
            user=User.objects.get(username=request.session['username'])
            if sort=='price htol':
                book=AvailBooks.objects.all().order_by('-b_price').exclude(uploader_name_id=user)
            elif sort=='price ltoh':
                book=AvailBooks.objects.all().order_by('b_price').exclude(uploader_name_id=user)
            elif sort=='recent':
                book=AvailBooks.objects.all().order_by('-id').exclude(uploader_name_id=user)
                book=book[:10]
            else:
                if book.count()==0:
                    msg='No items matched'
                elif book.count()==1:
                    book[:1].get()
        return render(request,'showbycategory.html',{'c':c,'book':book,'msg':msg})
    else:
        return HttpResponseRedirect('/loginm/login/')

def getbook(request):
    if 'username' in request.session:
        c={}
        c.update(csrf(request))
        bname=request.POST.get('hidden1','')
        uploader=request.POST.get('hidden2','')
        check=request.POST.get('check','')
        user=User.objects.get(username=uploader)
        book=AvailBooks.objects.get(b_name=bname,uploader_name_id=user)
        if check=='Show details':
            return render(request,'showdetails.html',{'img':book})
        elif check=='Add':
            list.append(book)
            return render(request,'buybook.html',c)
    else:
        return HttpResponseRedirect('/loginm/login/')

def viewcart(request):
    if 'username' in request.session:
        pri=0
        c={}
        c.update(csrf(request))
        for book in list:
            pri+=book.b_price
        return render(request,'viewcart.html',{'c':c,'list':list,'price':pri,'len':len(list)})
    else:
        return HttpResponseRedirect('/loginm/login/')

def remove(request):
    if 'username' in request.session:
        pri=0
        c={}
        c.update(csrf(request))
        bname=request.POST.get('hidden1','')
        uploader=request.POST.get('hidden2','')
        book=AvailBooks.objects.get(b_name=bname,uploader_name_id=uploader)
        if book in list:
            list.remove(book)
        for book in list:
            pri+=book.b_price
        return render(request,'viewcart.html',{'c':c,'list':list,'price':pri})
    else:
        return HttpResponseRedirect('/loginm/login/')

def confirmorder(request):
    if 'username' in request.session:
        uname=request.session['username']
        if len(list)!=0:
            for book in list:
                sbooks=SoldBooks(b_ISBN=book.b_ISBN,b_name=book.b_name,b_author=book.b_author,b_price=book.b_price,b_publisher=book.b_publisher,b_category=book.b_category,b_description=book.b_description,seller_name=book.uploader_name_id,buyer_name=uname,b_photo=book.b_photo)
                sbooks.save()
                book.delete()
            list.clear()
            return render(request,'orderconfirm.html',{'msg2':'Payment through cash','msg1':'Order has been placed successfully..'})
        else:
            return render(request,'orderconfirm.html',{'msg1':'Please select some book'})
    else:
        return HttpResponseRedirect('/loginm/login/')