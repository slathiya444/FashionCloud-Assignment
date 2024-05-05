import pytest

from FashionCloudProject.app.parsers.product_parser import ProductParser


@pytest.fixture
def uploaded_file_path():
    # Provide the path to the file on your computer
    return '/path/to/your/uploaded_file.csv'


def test_read_data_from_file(uploaded_file_path):
    parser = ProductParser(uploaded_file_path)
    data = parser.read_data()

    assert len(data) > 0
    # Add more assertions based on the expected content of your file


def test_parse_from_file(uploaded_file_path):
    parser = ProductParser(uploaded_file_path)
    single, multi = parser.parse({'Apple': 'Apples', 'Banana': 'Bananas'})

    # Add assertions based on the expected parsing result
