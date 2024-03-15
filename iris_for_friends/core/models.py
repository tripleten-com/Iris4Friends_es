from django.db import models


class PublishedModel(models.Model):
    """Abstract model. Adds a check in the is_published box."""
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True
