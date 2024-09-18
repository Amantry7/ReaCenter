from django.contrib import admin

from apps.secondary.models import About, AboutService, AboutDocument, Consultation, ConsultationProgres, Methods, MethodsEva, MethodsDev, Institution, MethodsEmp, ContactRequest
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
    
admin.site.register(ContactRequest)