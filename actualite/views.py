from django.shortcuts import render

# Create your views here.
def actualite_list(request):

    context = {}
    template_name = 'pages/actualite/actualite.html'
    return render(request, template_name, context)
