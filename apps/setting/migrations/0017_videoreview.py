# Generated by Django 5.1.1 on 2024-09-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0016_employe_certificate_employe_diplom_info_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('banner', models.ImageField(upload_to='video_reviews/', verbose_name='Баннер видео')),
                ('video', models.URLField(verbose_name='Видео')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Видео отзыв',
                'verbose_name_plural': 'Видео отзывы',
            },
        ),
    ]
