from django.shortcuts import render
from .models import TeamModel

# Create your views here.

def home(request):
    team = TeamModel.objects.all()
    data = {
        'teams' : team
    }
    return render(request, 'page/home.html', data)

def about(request):
    team = TeamModel.objects.all()
    data = {
        'teams' : team
    }
    return render(request, 'page/about.html', data)

def services(request):
    return render(request, 'page/services.html')

def contact(request):
    return render(request, 'page/contact.html')
