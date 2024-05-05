from django.db import models

from .base_models.mixins import UUIDGenerator
from .validators import validate_alphanumeric


class SizeMatrix(UUIDGenerator, models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=UUIDGenerator.generate_uuid,
        editable=False
    )

    size = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Size Group Code | Size",
        validators=[validate_alphanumeric],
    )

    size_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Size Name",
    )

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        # Check if size already exists (assuming size_group_code, size_code, and size_name are unique)
        existing_size = SizeMatrix.objects.filter(
            size=self.size,
            size_name=self.size_name
        ).first()

        if existing_size:
            # Use existing size
            self.pk = existing_size.pk  # Set primary key to connect existing object
        else:
            # Create new size
            super().save(*args, **kwargs)  # Call the original save method

        class Meta:
            verbose_name = "Size Matrix"
            verbose_name_plural = "Size Matrices"

