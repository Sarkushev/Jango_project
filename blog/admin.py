from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at', 'published_date']
    list_filter = ['category', 'created_at', 'author']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'