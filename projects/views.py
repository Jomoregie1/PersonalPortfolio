from django.shortcuts import render
from projects.models import Project


def all_projects(request):
    projects = Project.objects.all()
    return render(request, template_name='projects/all_projects.html'
                  , context={'projects': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html', {'project': project})
