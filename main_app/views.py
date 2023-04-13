from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', {'car': car})

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    template_name = 'cars/car_form.html'

class CarUpdate(UpdateView):
    model = Car
    fields = ('trim', 'color', 'description')
    template_name = 'cars/car_form.html'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'cars/car_confirm_delete.html'