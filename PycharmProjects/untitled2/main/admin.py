from django.contrib import admin
from main.models import User, Emoji


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'phone')


class EmojiAdmin(admin.ModelAdmin):
    list_display = ('emoji',)


admin.site.register(User, UserAdmin)
admin.site.register(Emoji, EmojiAdmin)
