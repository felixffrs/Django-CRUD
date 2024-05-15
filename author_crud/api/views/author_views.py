from author_crud.api.serializers.author_serializers import AuthorSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer

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
        author = self.get_queryset(pk)
        if author:
            author.delete()
            return Response({'message': f'Author {pk} deleted successfully'}, status = status.HTTP_204_NO_CONTENT)
        return Response({'message': f'Author {pk} not found'}, status = status.HTTP_400_BAD_REQUEST)

#List All Authors With their books (GET)
#Create new Auhor (POST)
# class AuthorListCreateAPIView(GeneralListCreateApiView):
#     serializer_class = AuthorSerializer

#List All Books (GET)
#Create new Book with its Author (POST)
# class BookListCreateAPIView(GeneralListCreateApiView):
#     serializer_class = BookSerializer

# class BookRetreiveAPIView(generics.RetrieveAPIView):
#     serializer_class = BookSerializer

#     def get_queryset(self):
#         model = self.get_serializer().Meta.model
#         return model.objects.all()
#     # def get(self, request, *args, **kwargs):
#     #     return super().get(request, *args, **kwargs)

# class BookReviewCreateAPIView(generics.RetrieveAPIView, generics.CreateAPIView):
#     serializer_class = ReviewSerializer  # Usa el serializer de Review para la creación de reviews

#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.all()

#     def get_object(self, pk):
#         return generics.get_object_or_404(Book, pk=pk)

#     def get(self, _, pk):
#         book = self.get_object(pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
    
#     def post(self, request, pk):

#         print(request.POST)

#         mutable_request = dict(request.data)

#         mutable_request['book'] = pk

#         print(mutable_request)

#         serializer = self.serializer_class(data = mutable_request)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, pk, *args, **kwargs):
    #     print(pk)
    #     mutable_data = dict(request.data)
    #     print(request.data)
        
    #     mutable_data['book'] = pk
    #     print(mutable_data)
    #     serializer = self.serializer_class(data = mutable_data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     # print("REQUESTTTT", request.data)
        # print(*args)
        # # print(**kwargs)
        # # Se llama al método post de CreateAPIView para manejar la operación de creación (POST)
        # book = self.get_object(pk)
        # print(book)
        # request.data['book'] = book.id  # Asignamos el libro a la review antes de la creación
        # return super().post(request, *args, **kwargs)

# @api_view(['GET', 'POST'])
# def author_api_view(request):

#     #Return all authors
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         authors_serializer = AuthorSerializer(authors, many=True)
#         return Response(authors_serializer.data, status=status.HTTP_200_OK)
    
#     #Create a new author
#     if request.method == 'POST':
#         author_serializer = AuthorSerializer(data=request.data)

#         if author_serializer.is_valid():
#             author_serializer.save()
#             return Response(author_serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detailed_api_view(request, id=None):
#     #Finding author by id
#     author = Author.objects.filter(id=id).first()

#     #Validating if author exist
#     if author:

#         #Return an author by id
#         if request.method == 'GET':
#             author_serializer = AuthorSerializer(author)
#             return Response(author_serializer.data, status=status.HTTP_200_OK)
        
#         #Update an author by id and json validated
#         if request.method == 'PUT':
#             author_serializer = AuthorSerializer(author, data=request.data)

#             if author_serializer.is_valid():
#                 author_serializer.save()
#                 return Response(author_serializer.data, status=status.HTTP_200_OK) 
            
#             return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         #Delete an author by id
#         if request.method == 'DELETE':
#             author.delete()
#             return Response({'message': f'Author {id} deleted successfully'}, status=status.HTTP_200_OK)

        
#     return Response({'message': f'Author {id} not found'}, status=status.HTTP_404_NOT_FOUND)