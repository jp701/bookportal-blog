from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.buy),
    url(r'^getcategory/$',views.getcategory),
    url(r'^getbook/$',views.getbook),
    url(r'^search/$',views.search),
    url(r'^viewcart/$',views.viewcart),
    url(r'^orderconfirm/$',views.confirmorder),
    url(r'^remove/$',views.remove),
]