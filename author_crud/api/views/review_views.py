from rest_framework import viewsets, status, generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from ...models.review import Review
from author_crud.api.serializers.review_serializers import ReviewSerializer, ReviewBookSerializer, ChangeReviewRatingSerializer

class BookReviewViewSet(viewsets.ModelViewSet):
    model = Review
    serializer_class = ReviewSerializer
    review_book_serializer_class = ReviewBookSerializer
    change_review_rating_serializer_class = ChangeReviewRatingSerializer

    def get_queryset(self, book_pk=None):
        if not book_pk:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(book_id = book_pk)
    
    def get_object(self, book_pk=None):
        pk = self.kwargs["pk"]
        return generics.get_object_or_404(self.model, pk=pk)

    @action(detail=True, methods=["PUT"], url_path="change-rating")
    def change_rating(self, request, book_pk, pk):
        serializer = self.change_review_rating_serializer_class(data=request.data)
        review = self.get_object(pk)

        if serializer.is_valid():
            review.rating = serializer.data["rating"]
            review.save()
            return Response({
                "message": f"Rating of review {pk} updated successfully"
            })
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, book_pk) -> Response:
        serializer = self.review_book_serializer_class(self.get_queryset(book_pk), many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request, book_pk) -> Response:
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, book_pk=None, pk=None):
        print(book_pk, pk)
        print(self.kwargs)
        review = self.get_object(pk)
        print(review)
        if review:
            serializer = self.serializer_class(review)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response({'message': f'Book {pk} not found'}, status = status.HTTP_400_BAD_REQUEST)
    