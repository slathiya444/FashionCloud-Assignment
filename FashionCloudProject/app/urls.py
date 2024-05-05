# urls.py
from django.urls import path
from .views import upload_files

urlpatterns = [
    path('upload/', upload_files, name='process_files'),
    path('result/', upload_files, name='process_files'),
]
