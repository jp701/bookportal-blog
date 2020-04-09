from django.db import models


# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=20,unique=True,primary_key=True)
    age=models.IntegerField(max_length=3)
    bdate=models.DateField('birthdate')
    hobby=models.CharField(max_length=20)

class User(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=10)
    p_name=models.CharField(max_length=50)
    mobile_no=models.IntegerField(max_length=10)
    email_id=models.CharField(max_length=50)
    address=models.CharField(max_length=100)


class SoldBooks(models.Model):
    b_ISBN=models.CharField(max_length=13,blank=True)
    b_name=models.CharField(max_length=50)
    b_author=models.CharField(max_length=40)
    b_price=models.FloatField()
    b_publisher=models.CharField(max_length=30,default='',blank=True)
    b_category=models.CharField(max_length=20,null=False,default='')
    b_description=models.TextField(max_length=150,default='')
    seller_name=models.CharField(max_length=30)
    buyer_name=models.CharField(max_length=30)
    date=models.DateField("Solddate",auto_now=True)
    b_photo=models.ImageField(upload_to='images/',default='') 

class AvailBooks(models.Model):
    b_ISBN=models.CharField(max_length=13,blank=True)
    b_name=models.CharField(max_length=50)
    b_author=models.CharField(max_length=40)
    b_price=models.FloatField()
    b_publisher=models.CharField(max_length=30,default='',blank=True)
    b_category=models.CharField(max_length=20,null=False)
    b_description=models.TextField(max_length=150,default='')
    uploader_name=models.ForeignKey(User,on_delete=models.CASCADE)
    b_photo=models.ImageField(upload_to='images/',default='')