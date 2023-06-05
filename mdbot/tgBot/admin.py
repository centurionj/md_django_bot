from django.contrib import admin

from .models import SendData, UserId

# Register your models here.


@admin.register(SendData)
class AdminSendData(admin.ModelAdmin):
    list_display = ('text', 'file', 'description')


@admin.register(UserId)
class AdminUserId(admin.ModelAdmin):
    list_display = ('name_from_tg', 'user_id')

