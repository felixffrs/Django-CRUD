from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from author_crud.api.views.author_views import AuthorViewSet
from author_crud.api.views.book_views import BookViewSet
from author_crud.api.views.review_views import BookReviewViewSet
from django.urls import path, include

# router = DefaultRouter()
# router.register(r'authors', AuthorViewSet, basename='authors')
# router.register(r'books', BookViewSet, basename='books')
# router.register(r'books/(?P<book_pk>[^/.]+)/reviews', BookReviewViewSet, basename='reviews')

# urlpatterns = router.urls

author_router = DefaultRouter()
author_router.register(r'authors', AuthorViewSet, basename='authors')
## generates:
# /authors/
# /authors/{pk}/

book_router = DefaultRouter()
book_router.register(r'books', BookViewSet, basename='books')
## generates:
# /books/
# /books/{pk}/

review_router = routers.NestedSimpleRouter(book_router, r'books', lookup='book')
#lookup -> creates a pk linked with the name wrote in the parameter example books/{boook_pk}
review_router.register(r'reviews', BookReviewViewSet, basename='reviews')
## generates:
# /books/{book_pk}/reviews/
# /books/{book_pk}/revews/{pk}/


urlpatterns = [
    path(r'', include(author_router.urls)),
    path(r'', include(book_router.urls)),
    path(r'', include(review_router.urls)),
]
