from django.conf.urls import url

from . import views,hbaserest
from django.contrib import admin
from . import  formaction

urlpatterns = [
    #url('', views.test, name='test'),
    url(r'^user/$', views.index, name='index'),
    url(r'^dau/$', hbaserest.dau_count, name='dau'),
    url(r'^city_user/$', formaction.get_user_month, name='ajax-dict'),
]