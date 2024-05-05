from django.db import models

from .base_models.mixins import UUIDGenerator
from .validators import validate_article


class Article(UUIDGenerator, models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=UUIDGenerator.generate_uuid,
        editable=False
    )

    article_structure = models.CharField(
        max_length=20,
        verbose_name="Article Structure Code",
    )

    article_number = models.CharField(
        max_length=5,
        verbose_name="Article Number",
        validators=[validate_article],
    )

    article_number_2 = models.CharField(
        max_length=25,
        verbose_name="Article Structure Code 2",
    )

    article_number_3 = models.CharField(
        max_length=25,
        verbose_name="Article Structure Code 3",
    )

    def __str__(self):
        return f"{self.article_structure} | {self.article_number}"
