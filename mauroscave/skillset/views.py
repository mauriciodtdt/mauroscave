from django.shortcuts import render
from .models import Skill


# Create your views here.
def skills(request):
    skills = Skill.objects.order_by('-date')
    return render(request, 'skillset/skills.html', {'skills': skills})
