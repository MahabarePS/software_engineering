from django.db import models
import uuid

class MenuModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    restaurant_name = models.CharField(max_length=225, unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.TextField()
    website = models.TextField(null=True)
    food_type = models.CharField(max_length=255, unique=True)
    food_name = models.CharField(max_length=255, unique=True)
    # Desserts, Cocktails
    category = models.CharField(max_length=100,unique=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant_name