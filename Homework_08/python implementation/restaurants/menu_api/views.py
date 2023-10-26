from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from menu_api.serializers import MenuSerializer
from menu_api.models import MenuModel

class ViewItem(ListAPIView):
    """This endpoint list all of the menus"""
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer

class CreateItem(CreateAPIView):
    """This endpoint allows for creation of an item"""
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer

class UpdateItem(UpdateAPIView):
    """This endpoint allows for updating a specific menu item by passing in the id of the menu to update"""
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer

class DeleteItem(DestroyAPIView):
    """This endpoint allows for deletion of a specific menu item from the database"""
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer