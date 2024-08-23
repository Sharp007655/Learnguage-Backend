from django.contrib import admin
from .models import *

# Register your models here.

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'language', 'mode')

class LanguageDataAdmin(admin.ModelAdmin):
    list_display = ('lang_ja', 'lang_en')

class AllWordDataAdmin(admin.ModelAdmin):
    list_display = ('word', 'read', 'mean', 'language')

class OriginalWordDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'word', 'read', 'mean')

class UserWordDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'word', 'count', 'quiz', 'correct', 'probability', 'period', 'hide')

class ModeDataAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(UserData, UserDataAdmin)
admin.site.register(LanguageData, LanguageDataAdmin)
admin.site.register(AllWordData, AllWordDataAdmin)
admin.site.register(OriginalWordData, OriginalWordDataAdmin)
admin.site.register(UserWordData, UserWordDataAdmin)
admin.site.register(ModeData, ModeDataAdmin)
