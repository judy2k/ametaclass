from django.db import models
from django.conf import settings

settings.configure()

class FoodRating(models.Model):
    food_name = models.CharField(max_length=255)
    rating = models.IntegerField()