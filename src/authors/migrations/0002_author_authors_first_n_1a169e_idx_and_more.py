# Generated by Django 5.1.4 on 2024-12-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='author',
            index=models.Index(fields=['first_name'], name='authors_first_n_1a169e_idx'),
        ),
        migrations.AddIndex(
            model_name='author',
            index=models.Index(fields=['last_name'], name='authors_last_na_679db7_idx'),
        ),
    ]
