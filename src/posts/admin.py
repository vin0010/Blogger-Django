from django.contrib import admin

# Register your models here.

from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"]
    list_display_links = ["title"]
    # lis
    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
