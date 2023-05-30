from django.db import models

from tgBot.functions.data_base_functions import DbFunc

# Create your models here.


class SendData(models.Model):
    obj = DbFunc()
    text = models.TextField('Текст', blank=True, null=True)
    file = models.FileField('Файл',  blank=True, null=True, upload_to=obj.get_upload_path)
    description = models.CharField('Описание', max_length=15, null=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['id']


class UserId(models.Model):
    name_from_tg = models.CharField('Имя в телеграм', max_length=15, null=True)
    user_id = models.CharField('Id', max_length=15, null=True)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['id']


obj = DbFunc()

obj.delete_files(SendData)
obj.replace_files(SendData)
