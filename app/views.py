from django.shortcuts import render

from app.models import Home
# Create your views here.
def home_list(request):
    home_list = Home.objects.all()
    context = {
        'hme_list': home_list
    }
    template_name = 'pages/app/home.html'
    return render(request, template_name, context)


def contact_view(request):
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
