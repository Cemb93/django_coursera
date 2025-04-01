from django.db import models

# Create your models here.
class Menu(models.Model):
  name = models.CharField(max_length=100)
  cuisine = models.CharField(max_length=100)
  price = models.IntegerField()

class DrinksCategory(models.Model):
  category_name = models.CharField(max_length = 200)

class Bebidas(models.Model):
  bebida = models.CharField(max_length=200)
  precio = models.IntegerField()
  category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)