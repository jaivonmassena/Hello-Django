from django.db import models


# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)