from django.urls import include, path

from app.views import home_views, economie_views, sante_views, securite_views, formation_views,  contact_views

app_name = 'app'
urlpatterns = [
    path('', home_views, name='home'),
    path('economie', economie_views, name='economie'),
    path('sante', sante_views, name='sante'),
    path('securite', securite_views, name='securite'),
    path('formation', formation_views, name='formation'),
    path('contact', contact_views, name='contact')
]
