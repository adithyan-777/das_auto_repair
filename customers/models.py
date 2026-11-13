from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone_number = PhoneNumberField(blank=True)