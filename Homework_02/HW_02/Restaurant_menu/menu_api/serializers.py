from django.db.models import fields
from rest_framework import serializers
from .models import Item

# converts the objects into data types that are understandable by javascript and front-end frameworks we need to use Serializer
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('restaurant', 'cuisine', 'cuisine_item', 'quantity','amount')