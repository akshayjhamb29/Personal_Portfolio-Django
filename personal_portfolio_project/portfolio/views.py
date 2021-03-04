from django.shortcuts import render
from .models import Project

def home(request):
    #grabs all the variables in project databases
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})