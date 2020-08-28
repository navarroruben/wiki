from django.urls import path
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.check_entry, name="check_entry"),
    path("search", views.search, name="search"),
    path("new_page", views.new_page, name="new_page"),
    path("edit_entry/<str:name>", views.edit_entry, name="edit_entry"),
    path("random_entry", views.random_entry, name="random_entry"),
]
