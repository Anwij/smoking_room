# Generated by Django 3.0.2 on 2020-04-05 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200405_0057'),
        ('sender', '0007_auto_20200405_0057'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='EmojiMessage',
        ),
        migrations.AlterModelOptions(
            name='emojimessage',
            options={'verbose_name': 'Смайлик-Сообщение', 'verbose_name_plural': 'Смайлик-Сообщения'},
        ),
    ]
