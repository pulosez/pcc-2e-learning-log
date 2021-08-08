from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(
        max_length=80,
    )
    text = models.TextField()
    date_added = models.DateTimeField(
        auto_now_add=True,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
