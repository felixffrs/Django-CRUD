from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from author_crud.api.serializer import AuthorSerializer, BookSerializer
from author_crud.models import Author, Book


@api_view(['GET', 'POST'])
def author_api_view(request):

    #Return all authors
    if request.method == 'GET':
        authors = Author.objects.all()
        authors_serializer = AuthorSerializer(authors, many=True)
        return Response(authors_serializer.data, status=status.HTTP_200_OK)
    
    #Create a new author
    if request.method == 'POST':
        author_serializer = AuthorSerializer(data=request.data)

        if author_serializer.is_valid():
            author_serializer.save()
            return Response(author_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def author_detailed_api_view(request, id=None):
    #Finding author by id
    author = Author.objects.filter(id=id).first()

    #Validating if author exist
    if author:

        #Return an author by id
        if request.method == 'GET':
            author_serializer = AuthorSerializer(author)
            return Response(author_serializer.data, status=status.HTTP_200_OK)
        
        #Update an author by id and json validated
        if request.method == 'PUT':
            author_serializer = AuthorSerializer(author, data=request.data)

            if author_serializer.is_valid():
                author_serializer.save()
                return Response(author_serializer.data, status=status.HTTP_200_OK) 
            
            return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #Delete an author by id
        if request.method == 'DELETE':
            author.delete()
            return Response({'message': f'Author {id} deleted successfully'}, status=status.HTTP_200_OK)

        
    return Response({'message': f'Author {id} not found'}, status=status.HTTP_404_NOT_FOUND)