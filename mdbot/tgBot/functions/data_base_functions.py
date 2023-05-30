from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver
from django.core.files.storage import default_storage

import os


class DbFunc:
    def get_upload_path(self, instance, filename):
        return os.path.join('mdbot/documents', filename)

    def delete_files(self, name):
        @receiver(pre_delete, sender=name)
        def delete_file(sender, instance, **kwargs):
            if instance.file:
                if instance.file:
                    file_path = instance.file.path
                    if default_storage.exists(file_path):
                        default_storage.delete(file_path)

    def replace_files(self, name):
        @receiver(pre_save, sender=name)
        def replace_old_file(sender, instance, **kwargs):
            if instance.pk:
                old_instance = name.objects.get(pk=instance.pk)

                if old_instance.file and old_instance.file != instance.file:
                    if old_instance.file:
                        file_path = old_instance.file.path
                        if default_storage.exists(file_path):
                            default_storage.delete(file_path)