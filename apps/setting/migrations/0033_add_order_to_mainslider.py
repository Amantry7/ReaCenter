from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0032_mainslider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainslider',
            options={'ordering': ['order'], 'verbose_name': 'Слайд главной страницы', 'verbose_name_plural': 'Слайды главной страницы'},
        ),
        migrations.AddField(
            model_name='mainslider',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок отображения'),
        ),
    ]
