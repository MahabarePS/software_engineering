# Import necessary modules and functions from Django and REST framework.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404

# Define a view function to provide an overview of available API endpoints.
@api_view(['GET'])
def ApiOverview(request):
    # Define a dictionary that maps endpoint names to their URLs.
    api_urls = {
        'all_items': '/',
        'Search by Restaurant': '/?restaurant=restaurant_name/', 
        'Search by Cuisine': '/?cuisine=cuisine_name/', 
        'Search by Cuisine item': '/?cuisine_item=cuisine_item_name/', 
        'Add': '/create/',  
        'Update': '/update/id/', 
        'Delete': '/item/id/delete/' 
    }
 
    # Return a Response containing the API endpoint dictionary.
    return Response(api_urls)

# Define a view function to add new items to the database.
@api_view(['POST'])
def add_items(request):
    # Serialize the incoming request data using ItemSerializer.
    item = ItemSerializer(data=request.data)
 
    # Check if an item with the same data already exists in the database.
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    # If the serialized data is valid, save the item and return its data in the response.
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        # Return a 404 status response if the data is not valid.
        return Response(status=status.HTTP_404_NOT_FOUND)

# Define a view function to view items based on query parameters.
@api_view(['GET'])
def view_items(request):
    # Check if there are query parameters in the URL.
    if request.query_params:
        # Filter items in the database based on the query parameters.
        items = Item.objects.filter(**request.query_params.dict())
    else:
        # If no query parameters are provided, retrieve all items.
        items = Item.objects.all()

    # If items are found, serialize them and return in the response.
    if items:
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        # Return a 404 status response if no items are found.
        return Response(status=status.HTTP_404_NOT_FOUND)

# Define a view function to update items based on a provided ID.
@api_view(['POST'])
def update_items(request, ob):
    # Get the item from the database based on the provided ID.
    item = Item.objects.get(ob=ob)
    
    # Serialize the incoming request data using ItemSerializer and specify the instance to update.
    data = ItemSerializer(instance=item, data=request.data)

    # If the serialized data is valid, save the updated item and return its data in the response.
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        # Return a 404 status response if the data is not valid.
        return Response(status=status.HTTP_404_NOT_FOUND)

# Define a view function to delete items based on a provided ID.
@api_view(['DELETE'])
def delete_items(request, ob):
    # Get the item from the database based on the provided ID, or return a 404 response if not found.
    item = get_object_or_404(Item, ob=ob)
    
    # Delete the item from the database.
    item.delete()
    
    # Return a 202 status response indicating successful deletion.
    return Response(status=status.HTTP_202_ACCEPTED)
