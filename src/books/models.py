from django.db import models

from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=128)
    count = models.PositiveIntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    class Meta:
        db_table = "books"
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['author']),
        ]

    def __str__(self) -> str:
        return self.title