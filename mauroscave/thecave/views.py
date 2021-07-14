from django.shortcuts import render, get_object_or_404
from .models import Project, Resource


def homepage(request):
    projects = Project.objects
    return render(request, 'thecave/home.html', {'projects': projects})


def detail(request, project_name):
    project_detail = get_object_or_404(Project, pk=project_name)
    resources = Resource.objects.filter(project=project_name).order_by('-date')
    return render(request, 'thecave/project.html', {'project': project_detail,
                                                    'resources': resources})
