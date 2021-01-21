from django.db import models
from customers.models import Customer

class FoodCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(FoodCategory, self).save(*args, **kwargs)

class FoodItem(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.IntegerField(blank=False)
    description = models.CharField(max_length=250, blank=False)
    veg = models.BooleanField(blank=False)
    category = models.ManyToManyField(FoodCategory)
    prep_time = models.IntegerField(blank=False)
    thumbnail = models.ImageField(blank=False)

    def __str__(self):
        return self.name

class Meal(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        mealitems = self.mealitem_set.all()
        total = sum([item.get_total for item in mealitems])
        return total
        
    @property
    def get_mealitems(self):
        mealitems = self.mealitem_set.all()
        return mealitems

    @property
    def get_cart_time(self):
        mealitems = self.mealitem_set.all()
        time = max([item.food_item.prep_time for item in mealitems])
        return time*2


class MealItem(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, blank=False)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, blank=False)
    quantity = models.IntegerField(default=0, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.food_item.price * self.quantity
        return total
