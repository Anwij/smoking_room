# Generated by Django 3.0.2 on 2020-04-04 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emoji',
            options={'verbose_name': 'Смайлик', 'verbose_name_plural': 'Смайлики'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='emoji',
            name='emoji',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Beer'), (1, 'Love'), (2, 'Shit')], unique=True),
        ),
    ]