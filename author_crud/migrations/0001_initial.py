# Generated by Django 5.0.1 on 2024-01-26 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('birth_date', models.DateField()),
                ('biography', models.TextField()),
            ],
        ),
    ]
