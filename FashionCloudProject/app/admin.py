from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Description
from .models import Mappings
from .models import Product
from .models import SizeMatrix

admin.site.register(Article)
admin.site.register(Description)
admin.site.register(Mappings)
admin.site.register(Product)
admin.site.register(SizeMatrix)
