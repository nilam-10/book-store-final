from django.contrib import admin
from .models import Book

# Register the Book model so it appears in the admin interface
admin.site.register(Book)
