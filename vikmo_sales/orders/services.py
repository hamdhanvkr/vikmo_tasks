from django.db import transaction
from inventory.models import Inventory

def confirm_order(order):
    if order.status != 'DRAFT':
        raise Exception("Only DRAFT orders can be confirmed")

    with transaction.atomic():
        insufficient = []

        for item in order.items.select_related('product'):
            try:
                inventory = Inventory.objects.select_for_update().get(
                    product=item.product
                )
            except Inventory.DoesNotExist:
                raise Exception({
                    "product": item.product.sku,
                    "error": "Inventory not initialized for this product"
                })

            if item.quantity > inventory.quantity:
                insufficient.append({
                    "product": item.product.sku,
                    "available": inventory.quantity,
                    "requested": item.quantity
                })

        if insufficient:
            raise Exception({
                "message": "Insufficient stock",
                "items": insufficient
            })

        # Deduct stock
        for item in order.items.all():
            inventory = Inventory.objects.select_for_update().get(
                product=item.product
            )
            inventory.quantity -= item.quantity
            inventory.save()

        order.status = 'CONFIRMED'
        order.save()


def deliver_order(order):
    if not order.can_deliver():
        raise Exception("Only CONFIRMED orders can be delivered")

    order.status = 'DELIVERED'
    order.save()
