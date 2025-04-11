from django.contrib import admin
from .models import Post, Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', "created_at")
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
