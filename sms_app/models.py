from django.db import models

class FormEntry(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    pickup_location = models.CharField(max_length=100)
    drop_location = models.CharField(max_length=100)
    cab_type = models.CharField(max_length=50)
    trip_type = models.CharField(max_length=50)
