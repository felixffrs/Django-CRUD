from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.TextField()
    birth_date = models.DateField()
    biography = models.TextField()
    class Meta:
        db_table = 'authors'

class Book(models.Model):
    title = models.TextField()
    pages = models.IntegerField()
    isbn_code = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta:
        db_table = 'books'
