from rest_framework import viewsets
from .serializer import AuthorSerializer, BookSerializer
from .models import Author, Book

# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer