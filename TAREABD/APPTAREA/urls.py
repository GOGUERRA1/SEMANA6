from django.urls import path

from . import views

urlpatterns = [
    path("APPTAREA/", views.index, name="index"),
]