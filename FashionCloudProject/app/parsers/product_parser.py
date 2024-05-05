import csv
from collections import defaultdict
from typing import List, Dict, Tuple, Any

from ..models import Product, Article, Description, SizeMatrix


class ProductParser:
    """
    Parses a Price Catalog file uploaded through a Django form.

    This class expects the uploaded file to be in a specific format .csv
    """

    def __init__(self, uploaded_file):
        """
        Initializes the parser with the uploaded file object.

        Args:
            uploaded_file (django.core.files.File): The uploaded file object from the form.
        """
        self.uploaded_file = uploaded_file
        self.data = []  # List to store parsed data

    def read_data(self) -> List[Dict]:
        """
        Reads the file content and create a dict
        :return:

        """
        try:
            with open(self.uploaded_file, 'r') as file:
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    self.data.append(row)
            return self.data
        except Exception as e:
            raise ValueError(f"Error parsing file: {e}")

    def parse(self, maps):
        """
        """
        if not self.read_data():
            raise ValueError("Uploaded file is empty")

        single_map, multi_map = maps
        product_map = {}
        objects_to_create = []

        for item in self.data:
            obj = {
                'ean': item.get('ean'),
                'supplier': item.get('supplier'),
                'brand': item.get('brand'),
                'catalog_code': item.get('catalog_code'),
                'collection': single_map['collection'].get(item.get('collection')) if 'collection' in single_map
                else multi_map['collection'].get(item.get('collection')),

                'currency': item.get('currency'),
                'price_buy_gross': item.get('price_buy_gross'),
                'price_buy_net': item.get('price_buy_net'),
                'discount_rate': item.get('discount_rate'),
                'price_sell': item.get('price_sell'),
            }

            article, _ = Article.objects.get_or_create(
                article_structure=single_map['article_structure_code'].get(item.get('article_structure_code'))
                if 'article_structure_code' in single_map
                else multi_map['article_structure_code'].get(item.get('article_structure_code')),
                article_number=item.get('article_number'),
                article_number_2=item.get('article_number_2'),
                article_number_3=item.get('article_number_3'),
            )

            size, _ = SizeMatrix.objects.get_or_create(
                size=single_map[item.get('size_group_code').get('size_code')] if 'size_group_code' in single_map
                else multi_map[item.get('size_group_code')].get('size_code'),
                size_name=item.get('size_name', None)
            )

            description, _ = Description.objects.get_or_create(
                season=single_map['season'].get(item.get('season')) if 'season' in single_map
                else multi_map['season'].get(item.get('season')),
                color=single_map['color_code'].get(item.get('color_code')) if 'color_code' in single_map
                else multi_map['color_code'].get(item.get('color_code')),
                material=item.get('material'),
                target_area=item.get('target_area'),
                size_matrix=size
            )
            # description.size_matrix = size
            obj['product_description'] = description
            obj['article'] = article

            objects_to_create.append(Product(**obj))

        created_obj = Product.objects.bulk_create(objects_to_create)
        return "The number of objects created:", {len(created_obj)}
