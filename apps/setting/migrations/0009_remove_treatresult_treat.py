# Generated by Django 5.1.1 on 2024-09-17 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0008_alter_reviews_create_at_treatresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatresult',
            name='treat',
        ),
    ]
