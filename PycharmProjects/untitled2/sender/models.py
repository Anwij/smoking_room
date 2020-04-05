from django.db import models
from main.models import User, Emoji


class EmojiMessage(models.Model):
    message = models.ForeignKey(Emoji, on_delete=models.DO_NOTHING)
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Emojisender')
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Emojireceiver')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Смайлик-Сообщение'
        verbose_name_plural = 'Смайлик-Сообщения'
