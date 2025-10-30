from django.contrib import admin
from django.utils.html import format_html
from .models import Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    # Fields visible in list view
    list_display = ('thumbnail', 'header', 'category', 'author', 'date_published')
    
    # Fields you can filter by
    list_filter = ('category', 'author', 'date_published')
    
    # Fields that can be searched
    search_fields = ('header', 'content', 'category', 'author')
    
    # Auto-generate slug from header
    prepopulated_fields = {'slug': ('header',)}
    
    # Order by most recent
    ordering = ('-date_published',)
    
    # Show date navigation
    date_hierarchy = 'date_published'
    
    # Field grouping for better layout
    fieldsets = (
        ('Post Information', {
            'fields': ('header', 'slug', 'category', 'author', 'image_url', 'content')
        }),
        ('Publication Details', {
            'fields': ('date_published',),
            'classes': ('collapse',),
        }),
    )

    # ✅ Add thumbnail preview in list
    def thumbnail(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="80" height="50" style="border-radius: 6px; object-fit: cover;" />', obj.image_url)
        return "No Image"
    thumbnail.short_description = "Preview"
