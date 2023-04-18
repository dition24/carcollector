from django.contrib import admin

# Register your models here.
from .models import Car, Mod

admin.site.register([Car, Mod])
