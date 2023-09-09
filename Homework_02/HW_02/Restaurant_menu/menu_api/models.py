from django.db import models

# Create Restaurant Menu model
class Item(models.Model):
    restaurant = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=255)
    cuisine_item = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    amount = models.FloatField()
 
    def __str__(self) -> str:
        return self.cuisine_item