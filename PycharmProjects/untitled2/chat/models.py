from django.db import models
from main.models import User


class Message(models.Model):
    message = models.CharField(max_length=200)
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='receiver')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
