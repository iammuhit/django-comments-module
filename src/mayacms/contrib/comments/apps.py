from django.apps import AppConfig


class CommentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mayacms.contrib.comments'
    verbose_name = "Comments"
