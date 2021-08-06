from django.db import models


class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(
        max_length=200,
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='entries',
    )
    text = models.TextField()
    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(f"{self.text}") > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text
