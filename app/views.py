from django.shortcuts import render,redirect
from django.contrib import messages # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from actualite.models import Actualite

# Create your views here.
def home_views(request):
    home_list = Actualite.objects.all().order_by('-created')[:1]
    home_laterale = Actualite.objects.all().order_by('-created')[:3]
    economie_list = Actualite.objects.filter(actu_categorie='ECONOMIE').order_by('-created')[:3]
    sante_list = Actualite.objects.filter(actu_categorie='SANTE').order_by('-created')[:3]
    securite_list = Actualite.objects.filter(actu_categorie='SECURITE').order_by('-created')[:3]
    formation_list = Actualite.objects.filter(actu_categorie='FORMATIONS').order_by('-created')[:3]
    context = {
        'home_list': home_list,
        'home_laterale': home_laterale,
        'economie_list': economie_list,
        'sante_list': sante_list,
        'securite_list': securite_list,
        'formation_list': formation_list
    }
    template_name = 'pages/app/home.html'
    return render(request, template_name, context)

def economie_views(request):
    economie_list = Actualite.objects.filter(actu_categorie='ECONOMIE').order_by('-created')
    context = {
        'economie_list': economie_list
    }
    template_name = 'pages/app/economie.html'
    return render(request, template_name, context)

def sante_views(request):
    sante = Actualite.objects.filter(actu_categorie='SANTE').order_by('-created')
    paginator = Paginator(sante, 12)
    page = request.GET.get('page')
    try:
        sante_list = paginator.page(page)
    except PageNotAnInteger:
        sante_list = paginator.page(1)
    except EmptyPage:
        sante_list = paginator.page(paginator.num_pages)
    context = {
        'sante_list': sante_list
    }
    template_name = 'pages/app/sante.html'
    return render(request, template_name, context)

def securite_views(request):
    securite = Actualite.objects.filter(actu_categorie='SECURITE').order_by('-created')
    paginator = Paginator(securite, 12)
    page = request.GET.get('page')
    try:
        securite_list = paginator.page(page)
    except PageNotAnInteger:
        securite_list = paginator.page(1)
    except EmptyPage:
        securite_list = paginator.page(paginator.num_pages)
    context = {
        'securite_list': securite_list
    }
    template_name = 'pages/app/securite.html'
    return render(request, template_name, context)


def formation_views(request):
    formation = Actualite.objects.filter(actu_categorie='FORMATIONS').order_by('-created')
    paginator = Paginator(formation, 12)
    page = request.GET.get('page')
    try:
        formation_list = paginator.page(page)
    except PageNotAnInteger:
        formation_list = paginator.page(1)
    except EmptyPage:
        formation_list = paginator.page(paginator.num_pages)
    context = {
        'formation_list': formation_list
    }
    template_name = 'pages/app/formation.html'
    return render(request, template_name, context)


def contact_views(request):
    if  request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        objet_name = request.POST['objet_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        message = request.POST['message']
        #print(first_name,last_name,objet_name,email_id,phone_num,message)
        if len(first_name)<3 or len(last_name)<3 or len(email_id)<5 or len(phone_num)<10 or len(message)<10:
            messages.error(request,'Svp, remplissez les champs correctement')
        else:
            contact_us = ContactForm(first_name=first_name,last_name=last_name,objet_name=objet_name,email_id=email_id,phone_num=phone_num,message=message)
            contact_us.save()
            messages.success(request, 'Merci! Nous avons réçu votre message')
            return redirect('/contact')

    template_name = 'pages/app/contact.html'
    return render(request, template_name, context=None)
