from django.contrib import admin
from .models import *


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "created")


admin.site.register(BlogPost, BlogPostAdmin)
