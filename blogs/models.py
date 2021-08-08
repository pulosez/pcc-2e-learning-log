from django.db import models


class BlogPost(models.Model):
    title = models.CharField(
        max_length=80,
    )
    text = models.TextField()
    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
