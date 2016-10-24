from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import Imovel
from django.shortcuts import render, get_object_or_404
from .forms import ImovelForm
from django.shortcuts import redirect
from django.template import *

def imovel_search(request):
	search = request.POST.get('search')
	imoveis_cidade = Imovel.objects.filter(cidade=search.lower())
	imoveis_estado = Imovel.objects.filter(estado=search.lower())
	return render(request, 'corretora/search.html', {'imoveis_cidade':imoveis_cidade, 'imoveis_estado':imoveis_estado})


def imovel_list(request):
	imoveis_al = Imovel.objects.filter(imovel='al')
	page = request.GET.get('page_al', 1)
	paginator = Paginator(imoveis_al, 4)
	search = request.POST.get('search')
	try:
		imoveis_al = paginator.page(page)
	except PageNotAnInteger:
		imoveis_al = paginator.page(1)
	except EmptyPage:
		imoveis_al = paginator.page(paginator.num_pages)

	imoveis_cp = Imovel.objects.filter(imovel='cp')
	page = request.GET.get('page_cp', 1)
	paginator = Paginator(imoveis_cp, 4)
	try:
		imoveis_cp = paginator.page(page)
	except PageNotAnInteger:
		imoveis_cp = paginator.page(1)
	except EmptyPage:
		posts_cp = paginator.page(paginator.num_pages)
	return render(request, 'corretora/imovel_list.html', {'imoveis_al':imoveis_al, 'imoveis_cp':imoveis_cp})


def imovel_detail(request, pk):
	imovel = get_object_or_404(imovel, pk=pk)
	imoveis = imovel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'corretora/imovel_detail.html', {'imovel': imovel, 'imoveis': imoveis})

def imovel_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            imovel = form.save(commit=False)
            imovel.author = request.user
            imovel.published_date = timezone.now()
            imovel.save()
            return redirect('corretora.views.imovel_detail', pk=imovel.pk)
    else:
        form = PostForm()
    return render(request, 'corretora/imovel_edit.html', {'form': form})

def imovel_edit(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            imovel = form.save(commit=False)
            imovel.author = request.user
            imovel.published_date = timezone.now()
            imovel.save()
            return redirect('corretora.views.imovel_detail', pk=imovel.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'corretora/imovel_edit.html', {'form': form})

def imovel_delete(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk).delete()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            imovel = form.save(commit=False)
            imovel.author = request.user
            imovel.published_date = timezone.now()
            imovel.save()
            return redirect('corretora.views.imovel_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'corretora/imovel_delete.html', {'form': form})


def admin_view(request):
	imoveis = Imovel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')	
	return render(request, 'corretora/admin.html', {'imoveis':imoveis})
