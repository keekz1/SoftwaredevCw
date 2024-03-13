# models.py

from django.db import models
from django.contrib.auth.models import User

class EquipmentBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment_name = models.CharField(max_length=100)
    booking_date = models.DateField()

class Stuff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stuff_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
