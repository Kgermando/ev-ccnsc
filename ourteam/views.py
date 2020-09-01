from django.shortcuts import render

from ourteam.models import OurTeam

# Create your views here.
def about_view(request):
    team_list = OurTeam.objects.all()
    context = {
        'team_list': team_list
    }
    template_name = 'pages/ourteam/about.html'
    return render(request, template_name, context)


def team_view(request, team_id):
    team = OurTeam.objects.get(id = team_id)
    context = {
        'team': team
    }
    template_name = 'pages/ourteam/team.html'
    return render(request, template_name, context)

