from django.shortcuts import render
from .models import Skill


# Create your views here.
def skills(request):
    skills = Skill.objects
    return render(request, 'skillset/skills.html', {'skills': skills})
