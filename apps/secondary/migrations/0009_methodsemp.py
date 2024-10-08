# Generated by Django 5.1.1 on 2024-09-18 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0008_institution'),
    ]

    operations = [
        migrations.CreateModel(
            name='MethodsEmp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('desc', models.CharField(max_length=255, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='methods_emp', verbose_name='Фото')),
                ('methods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='methods_emp', to='secondary.methods')),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонал',
            },
        ),
    ]
