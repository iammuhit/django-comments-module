from datetime import timezone
from django.db import models
from django.urls import reverse

class Comment(models.Model):
    post       = models.ForeignKey('posts.Post', related_name='comments', on_delete=models.CASCADE)
    author     = models.CharField(max_length=200)
    comment    = models.TextField()
    approved   = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('posts.index')

    def approve(self):
        self.approved = True
        self.save()
