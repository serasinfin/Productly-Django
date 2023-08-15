from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50)


class Product(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    stock = models.IntegerField()
    score = models.FloatField()
    # Date
    created_at = models.DateTimeField(default=timezone.now)
    # Relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE)