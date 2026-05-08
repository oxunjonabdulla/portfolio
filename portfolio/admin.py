from django.contrib import admin
from .models import Project, Experience, ContactMessage, Skill, Certificate


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'icon', 'order']
    list_editable = ['category', 'icon', 'order']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['category', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'order', 'created_at']
    list_editable = ['is_featured', 'order']
    list_filter = ['is_featured']
    search_fields = ['title', 'description']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date', 'is_current', 'order']
    list_editable = ['order', 'is_current']
    list_filter = ['is_current']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'year', 'is_verified', 'order']
    list_editable = ['is_verified', 'order']
    list_filter = ['is_verified', 'year']
    search_fields = ['title', 'issuer']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
