from django.conf.urls import url
from loginapp import views
from  django.contrib.staticfiles.urls import  staticfiles_urlpatterns

urlpatterns = [
    url(r'^login/$',views.login),
    url(r'^auth_user/$',views.auth_user),
    url(r'^invalid/$',views.invalid),
    url(r'^logout/$',views.logout),
    url(r'^delsession/$',views.delsession),
    url(r'^home/$',views.home),
    url(r'^aboutus/$',views.aboutus),
]

#urlpatterns +=staticfiles_urlpatterns()