from rest_framework.routers import DefaultRouter
from author_crud.api.views.author_views import AuthorViewSet
from author_crud.api.views.book_views import BookViewSet
from author_crud.api.views.review_views import BookReviewViewSet
from django.urls import path

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'books', BookViewSet, basename='books')
router.register(r'books/(?P<book_pk>[^/.]+)/reviews', BookReviewViewSet, basename='reviews')

urlpatterns = router.urls

# urlpatterns = router.urls + [
#     path('books/<int:book_pk>/reviews/', BookReviewViewSet.as_view({'get': 'list'}), name='book-reviews'),
# ]
