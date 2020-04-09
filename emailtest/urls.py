from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^forgotpass/$',views.forgotpass),
    url(r'^testit/$',views.testit),
    url(r'^gotoresetlink/$',views.gotoresetlink),
    url(r'^resetpassword/$',views.resetpassword),
]