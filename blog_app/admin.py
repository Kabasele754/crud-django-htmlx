from django.contrib import admin

from blog_app.models import Blog


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "image_tag", "description"]


admin.site.register(Blog,BlogAdmin)
