# Generated by Django 5.1.1 on 2024-09-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutdocument',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]
