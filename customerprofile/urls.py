from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.profile),
    url(r'^edit/$',views.editprofile),
    url(r'^updateprofile/$',views.updateprofile),
    url(r'^deleteprofile/$',views.deleteprofile),
    url(r'^uploaded/$',views.uploaded),
    url(r'^bought/$',views.bought),
    url(r'^sold/$',views.sold),
    url(r'^deleteAll/$',views.deleteall),
]