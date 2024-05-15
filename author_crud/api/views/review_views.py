from rest_framework import viewsets, status, generics
from rest_framework import status
from rest_framework.response import Response
from author_crud.api.serializers.book_serializers import BookSerializer
from author_crud.api.serializers.review_serializers import ReviewSerializer

class BookReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self, pk=None):
        print(pk, "ddsadsdas")
        if not pk:
            return self.get_serializer().Meta.model.objects.all()
        print(self.get_serializer().Meta.model.objects)
        return self.get_serializer().Meta.model.objects.filter(book_id = pk)
    
    # def get_object(self, pk):
    #     print(pk, "ewqeqwweqqew")
    #     return generics.get_object_or_404(Book, pk=pk)
    
    def list(self, request, book_pk) -> Response:
        serializer = self.get_serializer(self.get_queryset(book_pk), many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request, book_pk) -> Response:
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # def get(self, request, pk=None):
    #     book = self.get_object(pk)
    #     print(book, "dasdsasdaa")
    #     if book:
    #         serializer = BookSerializer(book)
    #         return Response(serializer.data, status = status.HTTP_200_OK)
    #     return Response({'message': f'Book {pk} not found'}, status = status.HTTP_400_BAD_REQUEST)
    