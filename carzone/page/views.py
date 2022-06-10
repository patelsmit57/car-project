from django.shortcuts import render
from .models import TeamModel
from cars.models import CarModel

# Create your views here.

def home(request):
    team = TeamModel.objects.all()
    feature_cars = CarModel.objects.order_by('-created_date').filter(is_featured = True)
    all_cars = CarModel.objects.order_by('-created_date')
    # search_fields = CarModel.objects.values('model', 'city', 'year', 'body_style')
    model_search = CarModel.objects.values_list('model', flat=True).distinct()
    city_search = CarModel.objects.values_list('city', flat=True).distinct()
    year_search = CarModel.objects.values_list('year', flat=True).distinct()
    body_style_search = CarModel.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams' : team,
        'feature_cars' : feature_cars,
        'all_cars' : all_cars,
        # 'search_fields' : search_fields,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search' : year_search ,
        'body_style_search' :  body_style_search,
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
