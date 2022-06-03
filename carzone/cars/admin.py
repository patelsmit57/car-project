from django.contrib import admin
from .models import CarModel
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))
    
    thumbnail.short_description = "car photo"
    list_display = ('id','thumbnail', 'car_title', 'state', 'year','price' ,'fuel_type','is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_featured',)
    search_field = ('id', 'car_title', 'city', 'model', 'fuel_type')
    list_filter = ('model', 'price', 'state')

admin.site.register(CarModel, CarAdmin)