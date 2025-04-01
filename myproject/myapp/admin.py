from django.contrib import admin
from .models import Bebidas
from .models import DrinksCategory

# Register your models here.
admin.site.register(Bebidas)
admin.site.register(DrinksCategory)