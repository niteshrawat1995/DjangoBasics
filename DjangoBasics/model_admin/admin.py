from django.contrib import admin

from .models import Source, Content, Tag
# Register your models here.


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
