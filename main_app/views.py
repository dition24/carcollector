from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Mod
from .forms import MaintenanceForm

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
    maintenance_form = MaintenanceForm()
    return render(request, 'cars/detail.html', {
        'car': car,
        'maintenance_form': maintenance_form
    })

def add_maintenance(request, car_id):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.car_id = car_id
        new_maintenance.save()

    return redirect('cars_detail', car_id=car_id)

def mods_index(request):
    mods = Mod.objects.all()
    return render(request, 'mods/index.html', {'mods': mods})

def mods_detail(request, mod_id):
    mod = Mod.objects.get(id=mod_id)
    return render(request, 'mods/detail.html', {'mod': mod})

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

class ModCreate(CreateView):
    model = Mod
    fields = '__all__'
    template_name = 'mods/mod_form.html'

class ModUpdate(UpdateView):
    model = Mod
    fields = '__all__'
    template_name = 'mods/mod_form.html'

class ModDelete(DeleteView):
    model = Mod
    success_url = '/mods/'
    template_name = 'mods/mod_confirm_delete.html'