from django.db import models

from .base_models.mixins import UUIDGenerator
from .size_matrix import SizeMatrix


class Description(UUIDGenerator, models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=UUIDGenerator.generate_uuid,
        editable=False
    )

    season = models.CharField(
        max_length=10,
        verbose_name="Season",
    )

    color = models.CharField(
        max_length=20,
        verbose_name="Color Name",
    )

    material = models.CharField(
        max_length=10,
        verbose_name="Material Used",
    )

    target_area = models.CharField(
        max_length=20,
        verbose_name="Target Area (Gender Specific)",
    )

    size_matrix = models.ForeignKey(
        SizeMatrix,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Size Matrix",
    )

    def __str__(self):
        return f"{self.season} | {self.color} | {self.size_matrix} "

    # def save(self, *args, **kwargs):
    #     # Check if size already exists (assuming size_group_code, size_code, and size_name are unique)
    #     existing_product = Description.objects.filter(
    #         season=self.season,
    #         color=self.color,
    #         target_area=self.target_area,
    #         size_matrix__size_name=self.size_matrix.size_name
    #     ).first()
    #
    #     if existing_product:
    #         # Use existing size
    #         self.pk = existing_product.pk  # Set primary key to connect existing object
    #     else:
    #         # Create new size
    #         super().save(*args, **kwargs)  # Call the original save method
    #
    #     class Meta:
    #         verbose_name = "Product Description"
    #         verbose_name_plural = "Product Description"

