from django.contrib import admin
from .models import FoodItem, Meal, MealItem, FoodCategory

admin.site.register(FoodItem)
admin.site.register(Meal)
admin.site.register(MealItem)
admin.site.register(FoodCategory)
