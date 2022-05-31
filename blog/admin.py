from django.contrib import admin
from .models import Post, Comment, Category


class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'slug', 'category', 'create_at', 'status']
    list_filter = ['category', 'create_at']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentItemInline]


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ['name', 'email', 'post']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
