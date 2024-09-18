from django.db import models
from django.utils.text import slugify


# Create your models here.
class Treat(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    subtitle = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Что мы лечим'
        verbose_name_plural='Что мы лечим'
   
class TreatResult(models.Model):
    title = models.CharField(
        max_length=244,
        verbose_name='Заголовок'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Результат'
        verbose_name_plural='Результаты'
     
class Service(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='service/',
        verbose_name='Фотография'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Услуга'
        verbose_name_plural='Услуги'
       
class ServiceImage(models.Model):
    service = models.ForeignKey(
        Service, related_name='service_image',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='service_image',
        verbose_name='Фото'
    )
    class Meta:
        verbose_name='Фото услуг'
        verbose_name_plural='Фото услуги'
 
class ServiceState(models.Model):
    service = models.ForeignKey(
        Service, related_name='service_state',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Услуги'
        verbose_name_plural='Услуги'
class Reviews(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name='Фамилия',
        blank=True, null=True
    )
    text = models.TextField(
        verbose_name='Отзыв',
        blank=True, null=True
    )
    is_approved = models.BooleanField(
        verbose_name='Одобрен',
        default=False
    )
    create_at = models.DateField(
        verbose_name='Дата',
        auto_now_add=True,
        blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        
class Employe(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='ФИО'
    )
    rols = models.CharField(
        max_length=255,
        verbose_name='Должность'
    )
    image = models.ImageField(
        upload_to='employe/',
        verbose_name='Фото'
    )
    image_2 = models.ImageField(
        upload_to='employe/',
        verbose_name='Фото 2',
        blank=True, null=True
    )
    diplom_info = models.TextField(
        verbose_name='Информация о дипломе',
        blank=True, null=True
    )
    evidence = models.TextField(
        verbose_name='Информация о свидетельстве',
        blank=True, null=True
    )
    certificate = models.TextField(
        verbose_name='Информация о сертификатах',
        blank=True, null=True
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Сотрудник',
        verbose_name_plural='Сотрудники'
        
class VideoReview(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='ФИО'
    )
    banner = models.ImageField(
        upload_to='video_reviews/',
        verbose_name='Баннер видео'
    )
    video = models.URLField(
        verbose_name='Видео'
    )
    create_at = models.DateField(
        verbose_name='Дата',
        auto_now_add=True
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Видео отзыв'
        verbose_name_plural='Видео отзывы'
        
class WriteReview(models.Model):
    image = models.ImageField(
        upload_to='write_riviews/',
        verbose_name='Фото отзыва'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='ФИО'
    )
    create_at = models.DateField(
        verbose_name='Дата',
        auto_now_add=True
    ) 
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Рукописный отзыв'
        verbose_name_plural='Рукописные отзывы'
        
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название сайта'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип сайта'
    )
    address = models.CharField(
        max_length=244,
        verbose_name='Адрес'
    )
    schedul = models.CharField(
        max_length=244,
        verbose_name='График работы'
    )
    youtube = models.URLField(
        verbose_name='Ссылка на youtube'
    )
    facebook = models.URLField(
        verbose_name='Cсылка на facebook'
    )
    instagram = models.URLField(
        verbose_name='Ссылка на instagram'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Настройки'
        verbose_name_plural='Настройки'
        
class SettingPhone(models.Model):
    setting = models.ForeignKey(
        Setting, related_name='setting_phone',
        on_delete=models.CASCADE
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    def __str__(self):
        return self.phone
    class Meta:
        verbose_name='Номер телефона'