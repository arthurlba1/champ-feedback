from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class champs(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=300)

    class Meta:
        ordering = ['name']