from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    logo = models.ImageField(upload_to="logo/", blank=True, null=True)