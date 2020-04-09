from django.conf.urls import url
from uploadbooks import views

urlpatterns = [
    url(r'^$',views.upload),
    url(r'^uploadeddetails/$',views.uploadeddetails),
    url(r'^getdetails/$',views.getdetails),
    url(r'^updatedetails/$',views.updatedetails),
]