from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'receiver_name', 'pub_date')
    ordering = ('pub_date',)
    
    def sender_name(self, obj):
        return obj.sender.name + ' ' + obj.sender.last_name

    def receiver_name(self, obj):
        return obj.receiver.name + ' ' + obj.receiver.last_name


admin.site.register(Message, MessageAdmin)

