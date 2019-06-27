from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = (
        'nickname', 'username', 'createDate', 'updateDate','type')
    list_display_links = ('nickname', 'username', 'createDate', 'updateDate')
    search_fields = ('nickname', 'username',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'date', 'sort', 'display')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('display', 'sort')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'user', 'hits', 'top', 'createDate','updateDate')
    list_filter = ('createDate', 'category', 'user', 'title')
    search_fields = ('title',)
    list_display_links = ('id','title')
    list_editable = ('top', 'category')
    list_per_page = 10
