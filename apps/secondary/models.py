from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

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
    desc_1 = RichTextUploadingField(
        verbose_name='Описание 1'
    )
    desc_2 = RichTextUploadingField(
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
    image = models.ImageField(
        upload_to='consult_progres/',
        verbose_name='Изображение',
        blank=True, null=True
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Консультация',
        verbose_name_plural='Консультация'
        
class Methods(models.Model):
    desc = RichTextField(
        verbose_name='Описание'
    )
    text = RichTextField(
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
    city = models.CharField(max_length=50, verbose_name='Город', default='Бишкек')

    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name} {self.last_name} ({self.city})"

    class Meta:
        verbose_name = 'Запрос на контакт'
        verbose_name_plural = 'Запросы на контакт'
        
        
class NewsBanner(models.Model):
    title = models.CharField(
        max_length=233,
        verbose_name='Заголовок'
    )
    subtitle = models.CharField(
        verbose_name='Подзаголовок',
        max_length=244
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Баннер новостей'
        verbose_name_plural='Баннер новостей'
        
class NewsBannerImage(models.Model):
    newsbanner = models.ForeignKey(
        NewsBanner, related_name='news_banner_image',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='news'
    )
    class Meta:
        verbose_name='Изобрежение для новостей'
        verbose_name_plural='Изобрежение для новостей'
        
class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    image = models.ImageField(
        upload_to='news_items/',
        verbose_name='Изображение'
    )
    short_description = models.TextField(
        verbose_name='Краткое описание', blank=True, null=True
    )
    content = RichTextUploadingField(
        verbose_name='Содержание', blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    published_at = models.DateField(
        verbose_name='Дата публикации',
        blank=True, null=True
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_at', '-created_at']

# Scientific Work Page Models
class ScientificWorkIntro(models.Model):
    """Model for the introduction section of the Scientific Work page"""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = RichTextField(verbose_name='Содержание')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Введение научной работы'
        verbose_name_plural = 'Введение научной работы'


class ScientificManual(models.Model):
    """Model for educational manuals in the Scientific Work page"""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='scientific/manuals/', verbose_name='Изображение')
    pdf_file = models.FileField(upload_to='scientific/manuals/pdf/', verbose_name='PDF файл', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок отображения')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Учебно-методическое пособие'
        verbose_name_plural = 'Учебно-методические пособия'
        ordering = ['order']


class ScientificPatent(models.Model):
    """Model for patents in the Scientific Work page"""
    patent_number = models.CharField(max_length=50, verbose_name='Номер патента')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='scientific/patents/', verbose_name='Изображение')
    pdf_file = models.FileField(upload_to='scientific/patents/pdf/', verbose_name='PDF файл', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок отображения')
    
    def __str__(self):
        return f'Патент №{self.patent_number}'
    
    class Meta:
        verbose_name = 'Патент'
        verbose_name_plural = 'Патенты'
        ordering = ['order']


class ScientificPermission(models.Model):
    """Model for permissions and certificates in the Scientific Work page"""
    PERMISSION_TYPES = [
        ('permission', 'Разрешение'),
        ('certificate', 'Свидетельство'),
    ]
    
    type = models.CharField(max_length=20, choices=PERMISSION_TYPES, default='permission', verbose_name='Тип документа')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='scientific/permissions/', verbose_name='Изображение')
    pdf_file = models.FileField(upload_to='scientific/permissions/pdf/', verbose_name='PDF файл', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок отображения')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Разрешение/Свидетельство'
        verbose_name_plural = 'Разрешения/Свидетельства'
        ordering = ['order']


class ScientificPublication(models.Model):
    """Model for scientific publications in the Scientific Work page"""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='scientific/publications/', verbose_name='Изображение')
    pdf_file = models.FileField(upload_to='scientific/publications/pdf/', verbose_name='PDF файл', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок отображения')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Научная публикация'
        verbose_name_plural = 'Научные публикации'
        ordering = ['order']


class ScientificPublicationsSection(models.Model):
    """Editable header/description for Publications section on Scientific Work page"""
    title = models.CharField(max_length=255, verbose_name='Заголовок раздела', default='Опубликованные научные и клинические исследования')
    description = models.TextField(verbose_name='Описание раздела', blank=True, null=True,
                                   help_text='Текст под заголовком в разделе публикаций')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Секция публикаций (заголовок и описание)'
        verbose_name_plural = 'Секция публикаций (заголовок и описание)'


class ScientificManualsSection(models.Model):
    """Editable header/description for Manuals section on Scientific Work page"""
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок раздела',
        default='Учебно-методические пособия'
    )
    description = models.TextField(
        verbose_name='Описание раздела',
        blank=True,
        null=True,
        help_text='Текст под заголовком в разделе учебно-методических пособий'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Секция пособий (заголовок и описание)'
        verbose_name_plural = 'Секция пособий (заголовок и описание)'


class ScientificPatentsSection(models.Model):
    """Editable header/description for Patents/Permissions section on Scientific Work page"""
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок раздела',
        default='Патенты, свидетельства и разрешения'
    )
    description = models.TextField(
        verbose_name='Описание раздела',
        blank=True,
        null=True,
        help_text='Текст под заголовком в разделе патентов/разрешений'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Секция патентов (заголовок и описание)'
        verbose_name_plural = 'Секция патентов (заголовок и описание)'


class ScientificJournalsSection(models.Model):
    """Editable header/description for Journals section on Scientific Work page"""
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок раздела',
        default='Научные журналы'
    )
    description = models.TextField(
        verbose_name='Описание раздела',
        blank=True,
        null=True,
        help_text='Текст под заголовком в разделе научных журналов'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Секция журналов (заголовок и описание)'
        verbose_name_plural = 'Секция журналов (заголовок и описание)'


class ScientificJournal(models.Model):
    """Model for scientific journals in the Scientific Work page"""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    image = models.ImageField(upload_to='scientific/journals/', verbose_name='Изображение')
    pdf_file = models.FileField(upload_to='scientific/journals/pdf/', verbose_name='PDF файл', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок отображения')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Научный журнал'
        verbose_name_plural = 'Научные журналы'
        ordering = ['order']