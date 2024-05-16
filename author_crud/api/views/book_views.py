from author_crud.api.serializers.book_serializers import BookSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self, pk=None):
        if not pk:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id = pk).first()

    def list(self, request) -> Response:
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request) -> Response:
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None) -> Response:
        if self.get_queryset(pk):
            serializer = self.get_serializer(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None) -> Response:
        book = self.get_queryset(pk)
        if book:
            book.delete()
            return Response({'message': f'Book {pk} deleted successfully'}, status = status.HTTP_204_NO_CONTENT)
        return Response({'message': f'Book {pk} not found'}, status = status.HTTP_400_BAD_REQUEST)