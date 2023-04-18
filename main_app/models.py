from django.db import models
from django.urls import reverse

# Create your models here.

class Mod(models.Model):
    name = models.CharField(max_length=50)
    gain = models.CharField(max_length=25)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('mods_detail', kwargs={'mod_id': self.id})

class Car(models.Model):
    year = models.IntegerField(default=0)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    trim = models.CharField(max_length=50, default='')
    color = models.CharField(max_length=50, default='primer')
    description = models.CharField(max_length=500, default='')
    
    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse('cars_detail', kwargs={'car_id': self.id})