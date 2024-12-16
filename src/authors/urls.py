from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authors.views import AuthorGenericViewSet


router = DefaultRouter()
router.register(r'authors', AuthorGenericViewSet)

urlpatterns = [
    path('', include(router.urls)),
]