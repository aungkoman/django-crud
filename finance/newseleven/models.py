from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    published_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    media = models.FileField()

    def __str__(self):
        return self.title