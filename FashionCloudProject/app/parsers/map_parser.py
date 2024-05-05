import csv
from collections import defaultdict
from typing import List, Dict, Tuple, Any


class MappParser:
    """
    Parses a mapping file uploaded through a Django form.

    This class expects the uploaded file to be in a specific format .csv in perticular
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

    def parse(self) -> Tuple[defaultdict, defaultdict]:
        """
          Processes file data and builds dictionaries using defaultdict.

          Args:
              file_data (list): A list of dictionaries containing source and destination data.

          Returns:
              tuple: A tuple containing two dictionaries:
                  - single_value_map: Stores data without '|' in source_type.
                  - multi_value_map: Stores data with '|' in source_type.
        :return: Tupple(DefaultDict, DefaultDict)
        """
        if not self.read_data():
            raise ValueError("Uploaded file is empty")

        single_value_map = defaultdict(dict)  # Use defaultdict(dict) for single values
        multi_value_map = defaultdict(dict)  # Use defaultdict(dict) for multi values

        for item in self.data:
            source_type = item['source_type']
            dest_type = item['destination_type']
            source_value = item['source']
            dest_value = item['destination']

            if '|' in source_type:
                split_source_value = source_value.split('|')
                multi_value_map[split_source_value[0]][split_source_value[1]] = dest_value
            else:
                # single_value_map[source_type][source_type] = dest_type  # Key for single value map
                single_value_map[source_type][source_value] = dest_value  # Value for single value map

        return single_value_map, multi_value_map
