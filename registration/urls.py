from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.regist),
    url(r'^doreg/$',views.doreg),
    #url(r'^confirmreg/$',views.confirmreg),
]
