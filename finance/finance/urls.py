from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("money/", include("money.urls")),
    path("admin/", admin.site.urls),
]