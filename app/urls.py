from django.urls import include, path

from app.views import home_list, contact_view

app_name = 'app'
urlpatterns = [
    path('', home_list, name='home'),
    path('contact', contact_view, name='contact')
]
