# app/views.py
from django.core.files.storage import FileSystemStorage
from django.db.models import Prefetch
from django.shortcuts import render
from .forms import FileUploadForm
from .models import Product, Article
from .parsers.map_parser import MappParser
from .parsers.product_parser import ProductParser


def upload_files(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            mapping_file = form.cleaned_data['mapping_file']
            main_file = form.cleaned_data['main_file']
            # main_file = request.FILES['main_file']
            # mapping_file = request.FILES.get('mapping_file')

            # read and parse mapping file, if present
            if mapping_file:
                file_path = read_data_from_form(mapping_file)
                mapper_class = MappParser(file_path)
                mapping_file_data = mapper_class.parse()

            # # Read main file
            main_file_path = read_data_from_form(main_file)
            product_class = ProductParser(main_file_path)
            product_data = product_class.parse(mapping_file_data)

            ## ORM to fetch all articles and associated products

            output = get_article_products()
            # context = {
            #     'output': output
            # }

            return render(
                request,
                'result.html',
                {
                    'message': 'Files processed successfully!',
                    'output': output
                })
    else:
        form = FileUploadForm()

    return render(request, 'upload.html', {'form': form})


def read_data_from_form(file):
    # Save the uploaded file temporarily
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    file_path = fs.path(filename)
    return file_path


def get_article_products():
    articles = Article.objects.all().prefetch_related(
        Prefetch('product_set', queryset=Product.objects.select_related('product_description'))
    )

    output = []
    for article in articles:
        article_output = f"Article Number: {article.article_number}\n"
        product_output = []
        for product in article.product_set.all():
            product_output.append(f"  - {product.ean} | {product.brand} | {product.supplier} | {product.product_description}")
        article_output += "\n".join(product_output)
        article_output += f"\n{article}"
        output.append(article_output)

    return "\n\n".join(output)