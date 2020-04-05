from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name + ' ' + self.last_name

class Emoji(models.Model):
    EMOJI_TYPES = (
        ('Beer', 'Beer'),
        ('Love', 'Love'),
        ('Shit', 'Shit')
    )
    emoji = models.CharField(max_length=12, choices=EMOJI_TYPES, unique=True)

    class Meta:
        verbose_name = 'Смайлик'
        verbose_name_plural = 'Смайлики'

    def __str__(self):
        return self.emoji
