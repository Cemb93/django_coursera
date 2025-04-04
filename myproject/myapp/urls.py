from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.home, name="home"),
  path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
  path('home/', views.home, name="home"),
  path('menu/', views.menu, name="menu"),
  path('about/', views.about, name="about"),
  path('book/', views.book, name="book"), 
] 