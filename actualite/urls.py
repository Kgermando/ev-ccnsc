from django.urls import include, path

from actualite.views import actualite_views, actualite_view_detail, actualite_views_province

app_name = 'actualite'
urlpatterns = [
    path('', actualite_views, name='actualite'),
    path('actualite-view/<int:id>', actualite_view_detail, name= 'actualite-view-detail'),
    path('province/<int:id>', actualite_views_province, name='province_'),
]
