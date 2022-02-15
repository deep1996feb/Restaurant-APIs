from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class restraunt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    direction = models.CharField(max_length=120, verbose_name="Direction")
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(restraunt, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    type = models.CharField(max_length=20,
                            choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('COFFEE', 'Coffee'),
                                     ('DINNER', 'Dinner')])
    thumbnail = models.ImageField(upload_to="recipe_thumbnails", default="recipe_thumbnails/default.png"),
    
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipe = models.ManyToManyField(Recipe)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")

    def __str__(self):
        return self.name

class DeliveryOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    dateadd = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

