from django.contrib import admin

from actualite.models import Actualite

admin.site.site_header = 'CCNSC-RDC ADMIN'
admin.site.site_title = "Interface d'administration de l'actualité"
# Register your models here.

class ActualiteAdmin(admin.ModelAdmin):
    list_display = (
        'actu_titre',
        'actu_province',
        'actu_categorie',
        'auteur',
        'created'
    )

    list_filter = (
        'actu_province',
        'actu_categorie',
        'auteur',
        'created')

    search_fields = ['actu_titre', 'actu_province', 'actu_categorie',]

    list_per_page = 50

admin.site.register(Actualite, ActualiteAdmin)
