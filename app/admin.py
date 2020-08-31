from django.contrib import admin

from app.models import  ContactForm

admin.site.site_header = 'CCNSC-RDC ADMIN'
admin.site.site_title = "Interface d'administration de l'Accueil"

# Register your models here.

class ContactFormAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'objet_name',
        'email_id',
        'phone_num',
        'created'
    )

    list_per_page = 50

admin.site.register(ContactForm, ContactFormAdmin)
