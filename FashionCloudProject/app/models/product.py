from django.db import models

from .article_matrix import Article
from .base_models.mixins import UUIDGenerator
from .description import Description
from .validators import validate_alphanumeric


class Product(UUIDGenerator, models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=UUIDGenerator.generate_uuid,
        editable=False
    )

    ean = models.IntegerField(
        max_length=20,
        verbose_name="European Article Number",
    )

    supplier = models.CharField(
        max_length=50,
        verbose_name="Supplier",
        validators=[validate_alphanumeric],
    )

    brand = models.CharField(
        max_length=25,
        verbose_name="Brand Name",
        validators=[validate_alphanumeric],
    )

    catalog_code = models.CharField(
        max_length=25,
        verbose_name="Catalog Code",
        blank=True,
        null=True,
    )

    collection = models.CharField(
        max_length=20,
        verbose_name="Collections",
        blank=True,
        null=True,
    )

    currency = models.CharField(
        max_length=5,
        verbose_name="Currency Code",
    )

    price_buy_gross = models.CharField(
        max_length=10,
        verbose_name="Gross Buying Price"
    )

    price_buy_net = models.CharField(
        max_length=10,
        verbose_name="Net Buying Price",
    )

    price_sell = models.CharField(
        max_length=10,
        verbose_name="Selling Price",
    )

    discount_rate = models.CharField(
        max_length=4,
        verbose_name="Discount Rate",
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name="Article details",
    )

    product_description = models.ForeignKey(
        Description,
        on_delete=models.CASCADE,
        verbose_name="Product Description",
    )

    def __str__(self):
        return f"{self.ean} | {self.brand} | {self.supplier}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
