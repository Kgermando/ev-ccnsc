from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from actualite.models import Actualite

class ActualiteSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Actualite.objects.all()

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['app:home', 'ourteam:about', 'app:contact', 'login', 'register', 'app:economie', 'app:sante', 'app:formation', 'app:securite']

    def location(self, item):
        return reverse(item)
