from django.urls import path
from menu_api import views

urlpatterns = [
    path("",views.ViewItem.as_view(),name="list_menu"),
    path("create/", views.CreateAPIView.as_view(),name="create_menu"),
    path("update/<str:pk>/",views.UpdateAPIView.as_view(),name="update_menu"),
    path("delete/<str:pk>/",views.DeleteItem.as_view(),name="delete_menu")
]