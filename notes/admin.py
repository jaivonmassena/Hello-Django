from django.contrib import admin
from .models import Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','created_at', 'last_modified', 'author')
    list_filter = ('title', 'created_at', 'author', 'last_modified')
    
admin.site.register(Note, NoteAdmin)
