import factory
from faker import Faker

from products.models import Product, Category
from stock.models import Stock
from user.models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.name()
    email = fake.email()
    password = fake.password()


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
