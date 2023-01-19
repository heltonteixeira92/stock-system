import pytest
from pytest_factoryboy import register

from tests.factories import ProductFactory

register(ProductFactory)


@pytest.fixture
def product(db, product_factory):
    product = product_factory.create()
    return product
