from django.shortcuts import render
from projects.models import Project


def all_projects(request):
    projects = Project.objects.all()
    return render(request, template_name='projects/all_projects.html'
                  , context={'projects': projects})
