import pytest
from pytest_factoryboy import register

from tests.factories import ProductFactory, StockFactory, CategoryFactory

register(ProductFactory)
register(StockFactory)
register(CategoryFactory)


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
