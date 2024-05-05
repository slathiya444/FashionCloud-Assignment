# Generated by Django 4.2.11 on 2024-05-04 20:17

import app.models.base_models.mixins
import app.models.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=app.models.base_models.mixins.UUIDGenerator.generate_uuid, editable=False, primary_key=True, serialize=False)),
                ('article_structure', models.IntegerField(max_length=5, verbose_name='Article Structure Code')),
                ('article_number', models.IntegerField(max_length=5, validators=[app.models.validators.validate_article], verbose_name='Article Structure Code')),
                ('article_number_2', models.CharField(max_length=25, verbose_name='Article Structure Code 2')),
                ('article_number_3', models.CharField(max_length=25, verbose_name='Article Structure Code 3')),
            ],
            bases=(app.models.base_models.mixins.UUIDGenerator, models.Model),
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.UUIDField(default=app.models.base_models.mixins.UUIDGenerator.generate_uuid, editable=False, primary_key=True, serialize=False)),
                ('season', models.CharField(max_length=10, verbose_name='Season')),
                ('color', models.CharField(max_length=10, verbose_name='Color Name')),
                ('material', models.CharField(max_length=10, verbose_name='Material Used')),
                ('target_area', models.CharField(max_length=20, verbose_name='Target Area (Gender Specific)')),
            ],
            bases=(app.models.base_models.mixins.UUIDGenerator, models.Model),
        ),
        migrations.CreateModel(
            name='SizeMatrix',
            fields=[
                ('id', models.UUIDField(default=app.models.base_models.mixins.UUIDGenerator.generate_uuid, editable=False, primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=50, validators=[app.models.validators.validate_alphanumeric], verbose_name='Size Group Code | Size')),
                ('size_name', models.CharField(max_length=100, verbose_name='Size Name')),
            ],
            bases=(app.models.base_models.mixins.UUIDGenerator, models.Model),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=app.models.base_models.mixins.UUIDGenerator.generate_uuid, editable=False, primary_key=True, serialize=False)),
                ('ean', models.IntegerField(max_length=20, verbose_name='European Article Number')),
                ('supplier', models.CharField(max_length=50, validators=[app.models.validators.validate_alphanumeric], verbose_name='Supplier')),
                ('brand', models.CharField(max_length=25, validators=[app.models.validators.validate_alphanumeric], verbose_name='Brand Name')),
                ('catalog_code', models.CharField(blank=True, max_length=25, null=True, verbose_name='Catalog Code')),
                ('collection', models.CharField(blank=True, max_length=20, null=True, verbose_name='Collections')),
                ('currency', models.CharField(max_length=5, verbose_name='Currency Code')),
                ('price_buy_gross', models.DecimalField(decimal_places=4, max_digits=10, max_length=10, verbose_name='Gross Buying Price')),
                ('price_buy_net', models.DecimalField(decimal_places=4, max_digits=10, max_length=10, verbose_name='Net Buying Price')),
                ('price_sell', models.DecimalField(decimal_places=4, max_digits=10, max_length=10, verbose_name='Selling Price')),
                ('discount_rate', models.DecimalField(decimal_places=2, max_digits=4, max_length=4, verbose_name='Discount Rate')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.article', verbose_name='Article details')),
                ('product_description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.description', verbose_name='Article details')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
            bases=(app.models.base_models.mixins.UUIDGenerator, models.Model),
        ),
        migrations.AddField(
            model_name='description',
            name='size_matrix',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.sizematrix', verbose_name='Size Matrix'),
        ),
    ]