from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Mod, Photo
from .forms import MaintenanceForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'car-collector-1108'

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cars_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})

@login_required
def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    maintenance_form = MaintenanceForm()
    car_mod_ids = car.mods.all().values_list('id')
    mods_car_doesnt_have = Mod.objects.exclude(id__in=car_mod_ids)
    return render(request, 'cars/detail.html', {
        'car': car,
        'maintenance_form': maintenance_form,
        'mods': mods_car_doesnt_have
    })

@login_required
def add_maintenance(request, car_id):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.car_id = car_id
        new_maintenance.save()

    return redirect('cars_detail', car_id=car_id)

@login_required
def assoc_mod(request, car_id, mod_id):
    car = Car.objects.get(id=car_id)
    car.mods.add(mod_id)
    return redirect('cars_detail', car_id=car_id)

@login_required
def unassoc_mod(request, car_id, mod_id):
    car = Car.objects.get(id=car_id)
    car.mods.remove(mod_id)
    return redirect('cars_detail', car_id=car_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cars_index')
        else:
            print(form.errors)
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error': error_message
    })

def add_photo(request, car_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, car_id=car_id)
        except Exception as error:
            print('photo upload failed')
            print(error)
    return redirect('cars_detail', car_id=car_id)

def mods_index(request):
    mods = Mod.objects.all()
    return render(request, 'mods/index.html', {'mods': mods})

def mods_detail(request, mod_id):
    mod = Mod.objects.get(id=mod_id)
    return render(request, 'mods/detail.html', {'mod': mod})

class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = '__all__'
    template_name = 'cars/car_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ('trim', 'color', 'description')
    template_name = 'cars/car_form.html'

class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'cars/car_confirm_delete.html'

class ModCreate(LoginRequiredMixin, CreateView):
    model = Mod
    fields = '__all__'
    template_name = 'mods/mod_form.html'

class ModUpdate(LoginRequiredMixin, UpdateView):
    model = Mod
    fields = '__all__'
    template_name = 'mods/mod_form.html'

class ModDelete(LoginRequiredMixin, DeleteView):
    model = Mod
    success_url = '/mods/'
    template_name = 'mods/mod_confirm_delete.html'