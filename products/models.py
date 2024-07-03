from django.db import models
from concurrency.fields import IntegerVersionField

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    version = IntegerVersionField()  # Added for optimistic locking

    def __str__(self):
        return self.name
