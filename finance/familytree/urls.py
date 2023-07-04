from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hello/", views.index, name="hello"),
    path("person-list/", views.helloWorld, name="person-list"),
    path("person-detail/<int:person_id>/", views.personDetail, name="person-detail"),
    path("test/",views.testFunc),
    path("html/", views.myHtml),
    path("greeting/", views.greeting),
    path("our-persons/", views.our_person_list)
]