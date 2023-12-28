from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        category_list = [
            {
                "name": "test_category",
                "description": "test_category description"
            }
        ]


        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Product(**category_item))

        Category.objects.bulk_create(category_for_create)
