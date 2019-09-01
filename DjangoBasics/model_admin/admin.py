from django.contrib import admin
from django.conf.urls import url

from .models import Source, Content, Tag
from .filters import HighOrderFilter, SaveCountFilter
# Register your models here.


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    date_hierarchy_drilldown = False
    list_filter = (HighOrderFilter, 'created_at')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'id', 'name', 'slug',
                    'created_by', 'modified_by')
    list_display_links = ('id', 'name', 'slug')
    list_filter = (SaveCountFilter, 'created_at', 'created_by')
    search_fields = ('slug', 'name')
    date_hierarchy = 'created_at'
    date_hierarchy_drilldown = False
    readonly_fields = ['save_count']

    exclude = ["created_by", "modified_by"]

    fieldsets = (
        ('BASIC', {
            'fields': ('name', 'slug', 'save_count')
        }),
        ('Relations', {
            'fields': ('source', 'tags'),
        }),
        ('Files', {
            'fields': ('icon', 'doc'),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.modified_by = request.user
        super(ContentAdmin, self).save_model(request, obj, form, change)

    def get_urls(self):
        urls = super(ContentAdmin, self).get_urls()
        my_urls = [
            url('newurl/', self.my_view)
        ]
        return my_urls + urls

    def my_view(self, request):
        # do something
        pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = ('is_active', )
