from django.shortcuts import render
from landing.models import Project


def all_projects(request):
    projects = Project.objects.all()
    return render(request, template_name='landing/index.html'
                  , context={'projects': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'landing/detail.html', {'project': project})
