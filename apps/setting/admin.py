from django.contrib import admin

from apps.setting.models import Treat, Service, Reviews, TreatResult, Employe, VideoReview, WriteReview, ServiceImage, ServiceState, Setting, SettingPhone
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

@admin.register(Treat)
class TreatAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

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
    list_display = ('name', 'video')
    
@admin.register(WriteReview)
class WriteReviewAdmin(admin.ModelAdmin):
    list_display = ('name', )
    
@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'logo')
    inlines = [SettingPhoneTaburInline]