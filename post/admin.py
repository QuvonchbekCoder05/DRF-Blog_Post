from django.contrib import admin
from .models import Blog, Comment, Category


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    search_fields = ('title', 'author__username')
    list_filter = ('category', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'user', 'created_at')
    search_fields = ('blog__title', 'user__username')
    list_filter = ('created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
