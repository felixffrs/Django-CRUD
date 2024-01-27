from rest_framework import serializers
from author_crud.models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "name", "birth_date", "biography")

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title")

