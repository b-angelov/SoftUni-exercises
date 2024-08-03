import os
from decimal import Decimal

import django
from django.core.exceptions import ValidationError

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Customer, Book, Product, DiscountedProduct, SpiderHero, FlashHero, Document

# Create queries within functions

if __name__ == '__main__':
    pass
    from django.contrib.postgres.search import SearchVector

    # Create the first 'Document' object with a title and content.
    document1 = Document.objects.create(
        title="Django Framework 1",
        content="Django is a high-level Python web framework for building web applications.",
    )

    # Create the second 'Document' object with a title and content.
    document2 = Document.objects.create(
        title="Django Framework 2",
        content="Django framework provides tools for creating web pages, handling URL routing, and more.",
    )

    # Update the 'search_vector' field in the 'Document' model with search vectors.
    Document.objects.update(search_vector=SearchVector('title', 'content'))

    # Perform a full-text search for documents containing the words 'django' and 'web framework'.
    results = Document.objects.filter(search_vector='django web framework')

    # Print the search results.
    for result in results:
        print(f"Title: {result.title}")
