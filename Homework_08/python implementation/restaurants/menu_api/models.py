from django.db import models
import uuid

class MenuModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    restaurant_name = models.CharField(max_length=225)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.TextField()
    website = models.TextField(null=True)
    # need to remove unique from food_ type and name
    food_type = models.CharField(max_length=255)
    food_name = models.CharField(max_length=255)
    quantity = models.PositiveBigIntegerField(default=1)
    amount = models.FloatField(default=0.00)
    # categorey = Desserts, Cocktails
    # categorey = models.CharField(max_length=100,null=True)
    # createdAt = models.DateTimeField(auto_now_add=True)
    # updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant_name