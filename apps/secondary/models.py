from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='ФИО'
    )
    rols = models.CharField(
        max_length=255,
        verbose_name='Должность'
    )
    image = models.ImageField(
        upload_to='about_emp/',
        verbose_name='Фото'
    )
    desc_1 = models.TextField(
        verbose_name='Описание 1'
    )
    desc_2 = models.TextField(
        verbose_name='Описание 2'
    )
    banner = models.ImageField(
        upload_to='about_banner/',
        verbose_name='Баннер'
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='О нас'
        verbose_name_plural='О нас'
        
class AboutService(models.Model):
    about = models.ForeignKey(
        About, related_name='about_service',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Услуги о нас'
        verbose_name_plural='Услуги о нас'
        
class AboutDocument(models.Model):
    about = models.ForeignKey(
        About, related_name='about_doc',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='about_doc/',
        verbose_name='Фото'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Сертификат'
        verbose_name_plural='Сертификаты'
        
class Consultation(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    subtitle = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок'
    )
    image = models.ImageField(
        upload_to='consultat',
        verbose_name='Фото'
    )
    def __str__(self):
        return self.title 
    class Meta:
        verbose_name='Консультация'
        verbose_name_plural='Консультация'
        
class ConsultationProgres(models.Model):
    consultation = models.ForeignKey(
        Consultation, related_name='consult_progres',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Консультация',
        verbose_name_plural='Консультация'
        
class Methods(models.Model):
    desc = models.TextField(
        verbose_name='Описание'
    )
    text = models.TextField(
        verbose_name='текс для внимание'
    )
    subtitle = models.CharField(
        max_length=255,
        verbose_name='Последний текст'
    )
    def __str__(self):
        return self.desc 
    class Meta:
        verbose_name='Метод',
        verbose_name_plural='Методы'
        
class MethodsEva(models.Model):
    methods = models.ForeignKey(
        Methods, related_name='methods_eva',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Эволюция'
        verbose_name_plural='Эволюция'
        
class MethodsDev(models.Model):
    methods = models.ForeignKey(
        Methods, related_name='methods_dev',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Приборы'
        verbose_name_plural='Приборы'
  
class MethodsEmp(models.Model):
    methods = models.ForeignKey(
        Methods, related_name='methods_emp',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255,
        verbose_name='ФИО'
    )
    desc = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='methods_emp',
        verbose_name='Фото'
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Персонал'
        verbose_name_plural='Персонал'
        
class Institution(models.Model):
    TEXT_POSITIONS = [
        ('top', 'Текст сверху'),
        ('bottom', 'Текст снизу'),
    ]

    name = models.CharField(max_length=255, verbose_name='Название учреждения')
    text_position = models.CharField(
        max_length=10,
        choices=TEXT_POSITIONS,
        default='none',
        verbose_name='Расположение текста'
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учреждение'
        verbose_name_plural = 'Учреждения'
        
class ContactRequest(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    appointment_date = models.CharField(max_length=255, verbose_name='Дата и время записи')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    description = models.TextField(verbose_name='Описание')

    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name} {self.last_name}"

    class Meta:
        verbose_name = 'Запрос на контакт'
        verbose_name_plural = 'Запросы на контакт'