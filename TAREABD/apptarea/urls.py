from django.urls import path

from . import views

urlpatterns = [
    path("productos", views.get_productos, name="get_productos"),
    path("add_producto", views.add_producto, name="add_producto"),
]