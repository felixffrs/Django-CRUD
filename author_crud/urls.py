from django.urls import path, include
from rest_framework import routers
from author_crud import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]