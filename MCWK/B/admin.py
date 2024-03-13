# admin.py

from django.contrib import admin
from .models import EquipmentBooking, Stuff

admin.site.register(EquipmentBooking)
admin.site.register(Stuff)
