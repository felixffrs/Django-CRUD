from rest_framework import serializers
from author_crud.api.serializers.review_serializers import ReviewSerializer
from author_crud.models.book import Book

class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'pages', 'isbn_code', 'author', 'reviews')