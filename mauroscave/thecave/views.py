from django.shortcuts import render, get_object_or_404
from .models import Project
from skillset.models import Skill


def homepage(request):
    projects = Project.objects
    return render(request, 'thecave/home.html', {'projects': projects})


def detail(request, project_name):
    project_detail = get_object_or_404(Project, pk=project_name)
    skills = Skill.objects.order_by('-date')
    return render(request, project_detail.project_url, {'project': project_detail,
                                                        'skills': skills})
