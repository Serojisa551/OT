from django.contrib import admin
from .models import *

class CommentsAdmin(admin.ModelAdmin):
    list_display = ["id", "comment_text", "author", "related_task"]

admin.site.register(Comments, CommentsAdmin)
