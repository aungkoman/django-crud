from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField()

class Author(models.Model):
    name = models.TextField()

class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    published_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    media = models.FileField()