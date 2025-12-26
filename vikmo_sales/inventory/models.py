from django.db import models
from products.models import Product

class Inventory(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='inventory'
    )
    quantity = models.PositiveIntegerField(default=0)

    updated_by = models.CharField(max_length=100, blank=True)  # bonus audit
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.sku} - {self.quantity}"
