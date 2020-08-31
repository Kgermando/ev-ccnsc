from django.db import models

from ccnsc.constant import CATEGORIES, PROVINCES
# Create your models here.

class Actualite(models.Model):
    actu_titre = models.CharField(max_length=300)
    auteur = models.CharField(max_length=300)
    actu_content = models.TextField()
    actu_province = models.CharField(max_length=300, choices=PROVINCES)
    actu_categorie = models.CharField(max_length=300, choices=CATEGORIES)
    actu_image = models.ImageField(upload_to='actu_img/')
    actu_image_1 = models.ImageField(upload_to='actu_img/', blank=True, verbose_name='Facultatif')
    actu_image_2 = models.ImageField(upload_to='actu_img/', blank=True, verbose_name='Facultatif')
    actu_image_3 = models.ImageField(upload_to='actu_img/', blank=True, verbose_name='Facultatif')
    created = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('actualite:actualite-view-detail', args=[str(self.id)])

    def __str__(self):
        return self.actu_titre

