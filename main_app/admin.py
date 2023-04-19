from django.contrib import admin

# Register your models here.
from .models import Car, Mod, Maintenance

admin.site.register([Car, Mod, Maintenance])
