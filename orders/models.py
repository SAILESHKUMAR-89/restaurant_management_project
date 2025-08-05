from django.db import models
from django.contrib.auth.models import User
from products.models import MenuItem

ORDER_STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('PREPARING', 'Preaparing'),
    ('DELIVERED', 'delivered'),
    ('CANCELLED', 'cancelled'),
]

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
