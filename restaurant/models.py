from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

 

class Restaurant(models.Model):
    image = models.ImageField( upload_to="static/images", height_field=None, width_field=None, max_length=None)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    address = models.CharField( max_length=250)
    def __str__(self):
        return self.name
    
class Review(models.Model):
    RAITING=(
        (1,"1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5"),
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RAITING)
    description = models.TextField()
