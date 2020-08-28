from django.urls import include, path

from economie.views import economie_list

app_name = 'economie'
urlpatterns = [
    path('', economie_list, name='economie')
]
