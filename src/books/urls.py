from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books.views import BookGenericViewSet


router = DefaultRouter()
router.register(r'books', BookGenericViewSet)


urlpatterns = [
    path('', include(router.urls)),
]