from django.urls import path
from . import views

urlpatterns = [
    # add first element to urlpatterns array
    # path function accept two parameter
    # first parameter is url path
    # second parameter is function name 
    path("", views.index),
    path("home-page/", views.home_page),
    path("our-new-html-page/", views.our_home_page)
]