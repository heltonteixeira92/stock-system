import pytest


def test_product_model_str(product):
    assert product.__str__() == 'embalagem grande'


def test_category_model(category):
    assert category.__str__() == 'embalagens'

