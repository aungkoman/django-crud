from django.contrib import admin

# Register your models here.

from .models import Category, Author, News

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(News)