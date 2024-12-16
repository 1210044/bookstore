from rest_framework import viewsets, mixins
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from authors.models import Author
from authors.serializers import AuthorSerializer


class AuthorGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Author.objects.all().prefetch_related('books')
    serializer_class = AuthorSerializer

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
