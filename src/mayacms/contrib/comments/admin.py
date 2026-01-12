from django.contrib import admin

from mayacms.contrib.comments.models import Comment


@admin.register(Comment)
class CommenntAdmin(admin.ModelAdmin):
    list_display = ['author', 'content_type', 'comment', 'approved', 'created_at']
