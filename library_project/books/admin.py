from django.contrib import admin
from .models import Book, Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'published_date', 'created_at', 'updated_at')
    list_filter = ('genre', 'published_date', 'created_at')
    search_fields = ('title', 'author', 'description')
    ordering = ('-published_date',)
    date_hierarchy = 'published_date'
    list_per_page = 20
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'author', 'genre', 'published_date')
        }),
        ('توضیحات', {
            'fields': ('description',)
        }),
        ('اطلاعات سیستمی', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
