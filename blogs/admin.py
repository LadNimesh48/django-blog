from django.contrib import admin
from .models import Category, Blog


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('title',) }
    list_display = ('title', 'category', 'author', 'status', 'is_featured', 'created_at',)
    search_fields = ('id', 'title', 'category__create_name', 'status', 'is_featured', 'created_at',)
    list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)