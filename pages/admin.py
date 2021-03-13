from django.contrib import admin
from django_mirror.admin import MirrorAdmin

from pages.models import Page


@admin.register(Page)
class PageAdmin(MirrorAdmin, admin.ModelAdmin):
    list_display = ('__str__', 'last_modified',)
    ordering = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'text',)
        }),
        ('Социални', {
            'classes': ('collapse',),
            'fields': ('social_image',)
        }),
        ('Хронология', {
            'classes': ('collapse',),
            'fields': ('created', 'last_modified',)
        }),
    )
    mirror_fields = ('text',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created', 'last_modified',)
