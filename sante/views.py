from django.shortcuts import render

# Create your views here.
def sante_list(request):

    context= {}
    template_name = 'pages/sante/sante.html'
    return render(request, template_name, context)
