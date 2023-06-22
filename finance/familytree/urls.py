from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("person-list/", views.helloWorld, name="person-list"),
]