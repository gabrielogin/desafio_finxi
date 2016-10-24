from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls import *

admin.site.index_template = 'admin/admin.html'
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.imovel_list),
	url(r'^search/$', views.imovel_search),
	url(r'^post/(?P<pk>[0-9]+)/$', views.imovel_detail),
	url(r'^post/(?P<pk>[0-9]+)/delete$', views.imovel_delete, name='imovel_delete'),
	url(r'^post/new/$', views.imovel_new, name='imovel_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.imovel_edit, name='imovel_edit'),
	url(r'^(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
]
