from django.contrib import admin

from ourteam.models import OurTeam
admin.site.site_header = 'CCNSC-RDC ADMIN'
admin.site.site_title = "Interface d'administration TEAM"
# Register your models here.
admin.site.register(OurTeam)
