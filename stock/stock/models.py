from django.db import models
from django.utils.translation import gettext_lazy as _
from products.models import Product


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name=_('product'))
    quantity = models.PositiveIntegerField(_('quantity'))
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    def __str__(self):
        return f'{self.quantity} {self.product} available'
