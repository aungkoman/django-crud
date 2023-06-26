from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("person-list/", views.helloWorld, name="person-list"),
    path("person-detail/<int:person_id>/", views.personDetail, name="person-detail"),
]