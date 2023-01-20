import pytest


@pytest.mark.django_db
def test_stock_model_str(stock):
    assert stock.__str__() == '10 embalagem grande available'
