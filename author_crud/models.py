from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.TextField()
    birth_date = models.DateField()
    biography = models.TextField()

class Book(models.Model):
    title = models.TextField()
    pages = models.IntegerField()
    isbn_code = models.TextField()
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
