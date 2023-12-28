from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content', 'is_published')
    search_fields = ('title', 'content',)
