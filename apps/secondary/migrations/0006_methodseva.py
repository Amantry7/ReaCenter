# Generated by Django 5.1.1 on 2024-09-18 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0005_methods'),
    ]

    operations = [
        migrations.CreateModel(
            name='MethodsEva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('methods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='methods_eva', to='secondary.methods')),
            ],
            options={
                'verbose_name': 'Эволюция',
                'verbose_name_plural': 'Эволюция',
            },
        ),
    ]
