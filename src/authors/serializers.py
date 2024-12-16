from rest_framework import serializers

from authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
