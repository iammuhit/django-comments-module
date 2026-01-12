from django.contrib.contenttypes import fields
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Comment(models.Model):
    object_id      = models.PositiveIntegerField()
    content_type   = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = fields.GenericForeignKey('content_type', 'object_id')

    author     = models.CharField(max_length=200)
    comment    = models.TextField()
    approved   = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments_comments'
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
        ]

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse(self.content_object.get_absolute_url())

    def approve(self):
        self.approved = True
        self.save()
