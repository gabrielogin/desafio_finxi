from django.conf.urls import patterns
from django.contrib import admin
from .models import Imovel
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import *


admin.site.register(Imovel)

def admin_view(request):
	posts = Imovel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')	
	return render(request, 'coretora/admin.html', {'posts':posts})

def get_admin_urls(urls):
    def get_urls():
        my_urls = patterns('',
            (r'^$', admin.site.admin_view(admin_view))
        )
        return my_urls + urls
    return get_urls

admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls
