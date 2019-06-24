from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = (
        'nickname', 'username', 'createDate', 'updateDate','type')
    list_display_links = ('nickname', 'username', 'createDate', 'updateDate')
    search_fields = ('nickname', 'username',)

