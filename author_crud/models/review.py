from django.db import models
from .base import BaseModel
from .book import Book

class Review(BaseModel):
    rating = models.IntegerField(null=False)
    description = models.TextField(blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    class Meta:
        db_table = 'reviews'
        verbose_name = 'Review'
        verbose_name = 'Reviews'
