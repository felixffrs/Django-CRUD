from django.db import models
from .base import BaseModel
from .author import Author

class Book(BaseModel):
    title = models.TextField(blank=False, null = False, unique = True)
    pages = models.IntegerField(blank=False, null = False)
    isbn_code = models.TextField(blank=False, null = False, unique = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'books'
        verbose_name = "Book"
        verbose_name_plural = "Books"
