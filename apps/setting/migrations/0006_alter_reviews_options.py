# Generated by Django 5.1.1 on 2024-09-17 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0005_reviews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
