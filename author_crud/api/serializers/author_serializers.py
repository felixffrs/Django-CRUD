from rest_framework import serializers
from author_crud.api.serializers.book_serializers import BookSerializer
from author_crud.models.author import Author

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'birth_date', 'biography', 'books')
