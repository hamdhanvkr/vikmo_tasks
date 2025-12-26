from django.db import transaction
from inventory.models import Inventory

def confirm_order(order):

    if order.status != 'DRAFT':
        raise Exception("Only DRAFT orders can be confirmed")

    insufficient = []

    for item in order.items.all():
        inventory = Inventory.objects.select_for_update().get(
            product=item.product
        )
        if item.quantity > inventory.quantity:
            insufficient.append({
                "product": item.product.sku,
                "available": inventory.quantity,
                "requested": item.quantity
            })

    if insufficient:
        raise Exception(insufficient)

    with transaction.atomic():
        for item in order.items.all():
            inventory = Inventory.objects.select_for_update().get(
                product=item.product
            )
            inventory.quantity -= item.quantity
            inventory.save()

        order.status = 'CONFIRMED'
        order.save()
