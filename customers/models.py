from django.db import models
from django.contrib.auth.models import User
import uuid

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.CharField(max_length=100, blank=False)
    employee_id = models.CharField(max_length=20, blank=False)
    mobile_number = models.CharField(max_length=15, blank=False)
    id_card = models.ImageField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    registration_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.user.username