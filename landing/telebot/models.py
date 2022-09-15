from django.db import models

# Create your models here.

class TeleSettings(models.Model):
    token = models.CharField(max_length=200, verbose_name='Token')
    chat = models.CharField(max_length=200, verbose_name="Chat id")
    message = models.TextField(verbose_name='Message text')

    def __str__(self):
        return self.chat

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'