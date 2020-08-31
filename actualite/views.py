from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from actualite.models import Actualite
# Create your views here.
def actualite_views(request):
    actualite_list = Actualite.objects.all().order_by('-created')[:1]
    actualite_list_laterale = Actualite.objects.all().order_by('-created')[:3]
    actu = Actualite.objects.all().order_by('-created')
    paginator = Paginator(actu, 9)
    page = request.GET.get('page')
    try:
        actu_relative = paginator.page(page)
    except PageNotAnInteger:
        actu_relative = paginator.page(1)
    except EmptyPage:
        actu_relative = paginator.page(paginator.num_pages)
    context = {
        'actualite_list': actualite_list,
        'actualite_list_laterale': actualite_list_laterale,
        'actu_relative': actu_relative
    }
    template_name = 'pages/actualite/actualite.html'
    return render(request, template_name, context)


def actualite_view_detail(request, id):
    actualite_list = Actualite.objects.get(id=id)
    actu = Actualite.objects.all().order_by('?')
    paginator = Paginator(actu, 9)
    page = request.GET.get('page')
    try:
        actu_relative = paginator.page(page)
    except PageNotAnInteger:
        actu_relative = paginator.page(1)
    except EmptyPage:
        actu_relative = paginator.page(paginator.num_pages)
    context = {
        "actualite_list": actualite_list,
        "actu_relative": actu_relative
    }
    template_name = 'pages/actualite/actualite-view.html'
    return render(request, template_name, context)


def actualite_views_province(request):
    actu = Actualite.objects.all()
    paginator = Paginator(actu, 9)
    page = request.GET.get('page')
    try:
        actu_province = paginator.page(page)
    except PageNotAnInteger:
        actu_province = paginator.page(1)
    except EmptyPage:
        actu_province = paginator.page(paginator.num_pages)
    context = {
        'actu_province': actu_province,
    }
    template_name = 'pages/actualite/actualite.html'
    return render(request, template_name, context)
