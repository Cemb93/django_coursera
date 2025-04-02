from django.contrib import admin
from .models import Bebidas, DrinksCategory, Booking, Employee

# Register your models here.
admin.site.register(Bebidas)
admin.site.register(DrinksCategory)
admin.site.register(Booking)
admin.site.register(Employee)