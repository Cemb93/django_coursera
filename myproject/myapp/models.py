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
  
class Booking(models.Model):
  first_name = models.CharField(max_length = 200)
  last_name = models.CharField(max_length = 200)
  guest_count = models.IntegerField()
  reservation_time = models.DateField(auto_now=True)
  comments = models.CharField(max_length=1000)
  
class Employee(models.Model):
  first_name = models.CharField(max_length = 200)
  last_name = models.CharField(max_length = 200)
  role = models.CharField(max_length = 100)
  shift = models.IntegerField()
  def __str__(self) -> str:
    return self.first_name