import pytest


@pytest.mark.django_db
def test_stock_model_str(product):
    assert product.__str__() == 'embalagem grande'
