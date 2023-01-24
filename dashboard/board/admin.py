from django.contrib import admin

from .models import Post, Comment, Category
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Comment)
admin.site.register(Category)
