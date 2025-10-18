from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from apps.setting.models import Treat, Service, Reviews, TreatResult, Employe, VideoReview, WriteReview, ServiceImage, ServiceState, Setting, SettingPhone, TreatImage, MainSlider, WhatsAppQR
# Register your models here.

class ServiceImageTaburInline(admin.TabularInline):
    model = ServiceImage
    extra = 1
    
class ServiceStateTaburInline(admin.TabularInline):
    model = ServiceState
    extra = 1
    
class SettingPhoneTaburInline(admin.TabularInline):
    model = SettingPhone
    extra = 1

class TreatImageTaburInline(admin.TabularInline):
    model = TreatImage
    extra = 1
class TreatAdminForm(forms.ModelForm):
    description2 = forms.CharField(widget=CKEditorUploadingWidget(), required=False)
    
    class Meta:
        model = Treat
        fields = '__all__'

@admin.register(Treat)
class TreatAdmin(admin.ModelAdmin):
    form = TreatAdminForm
    list_display = ('title', 'subtitle')
    inlines = [TreatImageTaburInline]

@admin.register(TreatResult)
class TreatAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    inlines = [ServiceImageTaburInline, ServiceStateTaburInline]
    
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')
    
@admin.register(Employe)
class EmploeAdmin(admin.ModelAdmin):
    list_display = ('name', 'rols')
    
@admin.register(VideoReview)
class VideoReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'video', 'create_at')
    readonly_fields = ('preview_thumbnail',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'video'),
            'description': 'Поддерживаются обычные YouTube видео и YouTube Shorts. Примеры ссылок:<br>'
                          '• https://www.youtube.com/watch?v=VIDEO_ID<br>'
                          '• https://youtu.be/VIDEO_ID<br>'
                          '• https://www.youtube.com/shorts/VIDEO_ID'
        }),
        ('Превью', {
            'fields': ('banner', 'preview_thumbnail'),
            'description': 'Баннер необязателен. Если не загружен, будет автоматически использовано превью из YouTube.'
        }),
    )
    
    def preview_thumbnail(self, obj):
        """Показывает превью видео в админке"""
        if obj.get_youtube_thumbnail():
            return f'<img src="{obj.get_youtube_thumbnail()}" style="max-width: 300px; height: auto;" />'
        return 'Превью недоступно'
    preview_thumbnail.short_description = 'Превью из YouTube'
    preview_thumbnail.allow_tags = True
    
@admin.register(WriteReview)
class WriteReviewAdmin(admin.ModelAdmin):
    list_display = ('name', )
    
@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'logo')
    inlines = [SettingPhoneTaburInline]

@admin.register(MainSlider)
class MainSliderAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(WhatsAppQR)
class WhatsAppQRAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)