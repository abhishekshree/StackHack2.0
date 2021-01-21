from django.shortcuts import render
from customers.models import Customer

def index(request):
    context = {}
    return render(request, 'index.html', context)