from django.contrib import admin
from .models.author import Author 
from .models.book import Book
from .models.review import Review

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)
