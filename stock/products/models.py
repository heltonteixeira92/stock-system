from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(_('name'), max_length=64)
    slug = models.SlugField(max_length=64)
    store_price = models.DecimalField(_('store price'), max_digits=5, decimal_places=2)
    sale_price = models.DecimalField(_('sale price'), max_digits=5, decimal_places=2)
    reference = models.CharField(_('reference'), max_length=120)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    stockable = models.BooleanField(_('stockable'), default=False)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.name
