# Generated by Django 5.1.1 on 2024-09-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0024_settingphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='treat',
            name='descrition',
            field=models.TextField(blank=True, null=True),
        ),
    ]
