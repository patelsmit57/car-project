from django.shortcuts import render
from .models import TeamModel
from cars.models import CarModel

# Create your views here.

def home(request):
    team = TeamModel.objects.all()
    feature_cars = CarModel.objects.order_by('-created_date').filter(is_featured = True)
    all_cars = CarModel.objects.order_by('-created_date')
    data = {
        'teams' : team,
        'feature_cars' : feature_cars,
        'all_cars' : all_cars,
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
