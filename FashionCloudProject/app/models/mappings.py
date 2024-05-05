from django.core.exceptions import ValidationError
from django.db import models

from .base_models.mixins import UUIDGenerator, CreatedAtMixin
from .validators import validate_alphanumeric


class Mappings(UUIDGenerator, CreatedAtMixin, models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=UUIDGenerator.generate_uuid,
        editable=False
    )

    src_value = models.CharField(
        max_length=50,
        verbose_name="Source Value",
        validators=[validate_alphanumeric],
    )

    dst_value = models.CharField(
        max_length=50,
        verbose_name="Destination Value",
        validators=[validate_alphanumeric],
    )

    src_type = models.CharField(
        max_length=50,
        verbose_name="Source Type",
        validators=[validate_alphanumeric],
    )

    dst_type = models.CharField(
        max_length=50,
        verbose_name="Destination Type",
        validators=[validate_alphanumeric],
    )

    created_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Source Value: {self.src_value} -> Destination Value: {self.dst_value}"

    class Meta:
        verbose_name = "Data Mapping"
        verbose_name_plural = "Data Mappings"
