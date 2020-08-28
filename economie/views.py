from django.shortcuts import render

# Create your views here.

def economie_list(request):

    context= {}
    template_name = 'pages/economie/economie.html'
    return render(request, template_name, context)