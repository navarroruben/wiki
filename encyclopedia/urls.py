from django.urls import path
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.title, name="title")
]
