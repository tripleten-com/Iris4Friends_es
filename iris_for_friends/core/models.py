from django.db import models


class PublishedModel(models.Model):
    """Modelo abstracto. Agrega un marca de verificación en el cuadro is_published."""
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True
