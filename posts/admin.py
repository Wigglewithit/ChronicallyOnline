from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "caption", "created_at", "is_active")
    list_filter = ("is_active", "created_at")
    search_fields = ("caption",)