from django.urls import path, include
from author_crud.api.api import author_api_view, author_detailed_api_view

urlpatterns = [
    path('authors/', author_api_view, name='authors_api_view'),
    path('authors/<int:id>', author_detailed_api_view, name='author_detailed_api_view'),
]