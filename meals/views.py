from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from .models import FoodItem, Meal, MealItem
def menu(request):
    food_items = FoodItem.objects.all()
    context = {
        'food_items':food_items
        }
    return render(request, 'menu.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        meal, created = Meal.objects.get_or_create(customer=customer, complete=False)
        meal_items = meal.mealitem_set.all()
    else:
        return redirect('login')

    context = {'meal_items':meal_items, 'meal':meal}
    return render(request, 'cart.html', context)

def updateItem(request):
    data = json.loads(request.body)
    item_id = data['item_id']
    action = data['action']
    customer = request.user.customer
    food_item = FoodItem.objects.get(id=item_id)

    meal, created = Meal.objects.get_or_create(customer=customer, complete=False)
    meal_item, created = MealItem.objects.get_or_create(meal=meal, food_item=food_item)

    if action == 'add':
        meal_item.quantity = (meal_item.quantity + 1)
    elif action == 'remove':
        meal_item.quantity = (meal_item.quantity - 1)
    
    meal_item.save()

    if meal_item.quantity <= 0:
        meal_item.delete()

    print(food_item)
    return JsonResponse("Item was added", safe=False)

def admin_dashboard(request):
    orders = Meal.objects.filter(complete=True)
    context = {"orders":orders}
    return render(request, 'admin-dashboard.html', context)