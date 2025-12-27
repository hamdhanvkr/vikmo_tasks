from django.db import models
from dealers.models import Dealer
from products.models import Product
from inventory.models import Inventory
from django.db import transaction

class Order(models.Model):
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('CONFIRMED', 'Confirmed'),
        ('DELIVERED', 'Delivered'),
    ]

    order_number = models.CharField(max_length=30, unique=True, db_index=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.PROTECT, related_name='orders')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def can_confirm(self):
        return self.status == 'DRAFT'

    def can_deliver(self):
        return self.status == 'CONFIRMED'

    def delete(self, *args, **kwargs):
        if self.status == 'CONFIRMED':
            with transaction.atomic():
                for item in self.items.all():
                    inventory = Inventory.objects.select_for_update().get(
                        product=item.product
                    )
                    inventory.quantity += item.quantity
                    inventory.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        self.line_total = self.quantity * self.unit_price
        super().save(*args, **kwargs)
