from django.shortcuts import redirect, render
from .models import ContactModel
from django.contrib import messages

# Create your views here.

def inquriy(request):
    if request.method == "POST":
        car_id = request.POST['car_id']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contact = ContactModel.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contact:
                messages.error(request, 'You have already made an inquriry about this car. Please wait untill we get back to you.')
                return redirect('/cars/'+car_id)

        contact = ContactModel(car_id=car_id, user_id=user_id, first_name=first_name, 
                                last_name=last_name, customer_need=customer_need, car_title=car_title,
                                city=city, state=state, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/'+car_id)
