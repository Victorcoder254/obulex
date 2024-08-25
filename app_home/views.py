from django.shortcuts import render
from .models import *

def home_view(request):
    # Querying all the data from the models
    services = service.objects.last()  # Assuming you want the latest service entry
    about_us_info = about_us.objects.last()  # Assuming you want the latest about_us entry
    project_info = projects.objects.last()  # Assuming you want the latest project entry
    team_info = Team.objects.last()  # Assuming you want the latest team entry
    footer_info = FooterContactInfo.objects.last()  # Assuming you want the latest footer entry

    # Creating context to pass to the template
    context = {
        'services': services,
        'about_us_info': about_us_info,
        'project_info': project_info,
        'team_info': team_info,
        'footer_info': footer_info,
    }

    # Rendering the home.html template with the context
    return render(request, 'files/home.html', context)
