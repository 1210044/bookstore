from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    class Meta:
        db_table = "authors"
        indexes = [
            models.Index(fields=['first_name']),
            models.Index(fields=['last_name']),
        ]

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'