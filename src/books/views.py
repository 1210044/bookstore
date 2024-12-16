from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from books.models import Book
from books.serializers import BookSerializer
from books.paginations import BookPagination


class BookGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer
    pagination_class = BookPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def buy(self, request, pk=None):
        book = self.get_object()
        if book.count > 0:
            book.count -= 1
            book.save()
            return Response({'status': 'Book purchased'}, status=status.HTTP_200_OK)
        return Response({'error': 'The books are out'}, status=status.HTTP_400_BAD_REQUEST)