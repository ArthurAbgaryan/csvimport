# Generated by Django 3.2.24 on 2024-06-01 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_bookimport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=150, null=True),
        ),
    ]