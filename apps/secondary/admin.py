from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from apps.secondary.models import (About, AboutService, AboutDocument, Consultation, ConsultationProgres, 
    Methods, MethodsEva, MethodsDev, Institution, MethodsEmp, ContactRequest, NewsBanner, 
    NewsBannerImage, News, ScientificWorkIntro, ScientificManual, ScientificPatent, 
    ScientificPermission, ScientificPublication, ScientificPublicationsSection, 
    ScientificManualsSection, ScientificPatentsSection, ScientificJournalsSection, ScientificJournal)
# Register your models here.

class AboutServiceTabularInline(admin.TabularInline):
    model = AboutService
    extra = 1
    
class AboutDocTabularInline(admin.TabularInline):
    model = AboutDocument
    extra = 1
    
class MethodsEvaTabularInline(admin.TabularInline):
    model = MethodsEva
    extra = 1

class MethodsDevTabularInline(admin.TabularInline):
    model = MethodsDev
    extra = 1
    
class MethodsEmpTabularInline(admin.TabularInline):
    model = MethodsEmp
    extra = 1

class ConsultationProgresTabularInline(admin.TabularInline):
    model = ConsultationProgres
    extra = 2
    
class NewsBannerImageTabularInline(admin.TabularInline):
    model = NewsBannerImage
    extra = 1
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('desc_1', 'desc_2')
    inlines = [AboutServiceTabularInline, AboutDocTabularInline]
    
@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    inlines = [ConsultationProgresTabularInline]
    
@admin.register(Methods)
class MethodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'desc')
    inlines = [MethodsEvaTabularInline, MethodsDevTabularInline, MethodsEmpTabularInline]
    
@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(NewsBanner)
class NewsBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle')
    inlines = [NewsBannerImageTabularInline]
    
admin.site.register(ContactRequest)

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = News
        fields = '__all__'

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('title', 'published_at', 'created_at', 'is_published')

# Scientific Work Admin Registration
@admin.register(ScientificWorkIntro)
class ScientificWorkIntroAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ScientificManual)
class ScientificManualAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'order')
    list_editable = ('order',)
    
@admin.register(ScientificPatent)
class ScientificPatentAdmin(admin.ModelAdmin):
    list_display = ('patent_number', 'title', 'description', 'order')
    list_editable = ('order',)
    
@admin.register(ScientificPermission)
class ScientificPermissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'description', 'order')
    list_editable = ('order',)
    list_filter = ('type',)
    
@admin.register(ScientificPublication)
class ScientificPublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'order')
    list_editable = ('order',)
    
@admin.register(ScientificPublicationsSection)
class ScientificPublicationsSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ScientificManualsSection)
class ScientificManualsSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ScientificPatentsSection)
class ScientificPatentsSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ScientificJournalsSection)
class ScientificJournalsSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ScientificJournal)
class ScientificJournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
