import factory
from faker import Faker
from products.models import Product

from products.models import Category

from stock.models import Stock

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'embalagens'


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "embalagem grande"
    slug = "embalagem-grande"
    store_price = 1.99
    sale_price = 2.99
    category = factory.SubFactory(CategoryFactory)


class StockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Stock

    product = factory.SubFactory(ProductFactory)
    quantity = 10
