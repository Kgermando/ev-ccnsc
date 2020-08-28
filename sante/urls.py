from django.urls import include, path

from sante.views import sante_list

app_name = 'sante'
urlpatterns = [
    path('', sante_list, name='sante')
]
