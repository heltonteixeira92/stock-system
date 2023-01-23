import pytest
from pytest_factoryboy import register

from tests.factories import ProductFactory, StockFactory, CategoryFactory, UserFactory

register(ProductFactory)
register(StockFactory)
register(CategoryFactory)
register(UserFactory)


@pytest.fixture
def user(db, user_factory):
    user = user_factory.create()
    return user


@pytest.fixture
def category(db, category_factory):
    category = category_factory.create()
    return category


@pytest.fixture
def product(db, product_factory):
    product = product_factory.create()
    return product


@pytest.fixture
def stock(db, stock_factory):
    stock = stock_factory.create()
    return stock
