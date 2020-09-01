from django.contrib import admin

from ourteam.models import OurTeam
admin.site.site_header = 'CCNSC-RDC ADMIN'
admin.site.site_title = "Interface d'administration TEAM"
# Register your models here.
class OurTeamAdmin(admin.ModelAdmin):
    list_display = (
        'team_name',
        'team_designation',
        'team_created_date',
        'team_updated_date'
    )

    list_filter = (
        'team_name',
        'team_designation',
        'team_created_date'
        )

    search_fields = ['team_name', 'team_designation', 'team_created_date',]

    list_per_page = 50

admin.site.register(OurTeam, OurTeamAdmin)
