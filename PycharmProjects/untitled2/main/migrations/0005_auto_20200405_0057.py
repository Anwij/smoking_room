# Generated by Django 3.0.2 on 2020-04-04 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200405_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emoji',
            name='emoji',
            field=models.CharField(choices=[('Beer', 'Beer'), ('Love', 'Love'), ('Shit', 'Shit')], max_length=12, unique=True),
        ),
    ]
