from django.urls import include, path

from actualite.views import actualite_list

app_name = 'actualite'
urlpatterns = [
    path('', actualite_list, name='actualite')
]
