# Generated by Django 3.0.2 on 2020-04-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0003_remove_message_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
