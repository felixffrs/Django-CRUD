# Generated by Django 5.0.1 on 2024-02-03 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author_crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_code',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(unique=True),
        ),
    ]