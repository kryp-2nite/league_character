from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Champion, Abilities # import the Artist model from models.py
# Register your models here.

admin.site.register(Champion) # this line will add the model to the admin panel
admin.site.register(Abilities) 
