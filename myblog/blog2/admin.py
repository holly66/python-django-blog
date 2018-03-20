from django.contrib import admin
from models import BlogArticles


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title","author","publish")
    list_filed =("publish", "author")
    search_field = ('title', "body")
    raw_id_field = ("author",)
    date_hierarchy = "publish"
    ordering = ['publish', 'author']
admin.site.register(BlogArticles,BlogArticlesAdmin)
# Register your models here.
