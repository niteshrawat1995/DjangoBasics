from django.contrib import admin

from .models import Source, Content, Tag
# Register your models here.


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_by', 'modified_by')
    list_display_links = ('id', 'name', 'slug')
    list_filter = ('created_at', 'created_by')
    search_fields = ('slug', 'name')

    fieldsets = (
        ('BASIC', {
            'fields': ('name', 'slug')
        }),
        ('Relations', {
            'fields': ('source', 'tags'),
        }),
        ('Files', {
            'fields': ('icon', 'doc'),
        }),
        ('Authors', {
            'fields': ('created_by', 'modified_by'),
        }),
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
