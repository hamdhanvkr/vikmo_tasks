from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'unit_price', 'line_total']
        read_only_fields = ['unit_price', 'line_total']

    def validate(self, data):
        if self.instance and self.instance.order.status != 'DRAFT':
            raise serializers.ValidationError(
                "Cannot modify items of a non-DRAFT order"
            )
        return data


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['order_number', 'total_amount', 'status']

    def validate(self, data):
        if self.instance and self.instance.status != 'DRAFT':
            raise serializers.ValidationError(
                "Only DRAFT orders can be modified"
            )
        return data

    def create(self, validated_data):
        items_data = validated_data.pop('items')

        import datetime
        today = datetime.date.today().strftime("%Y%m%d")
        count = Order.objects.filter(created_at__date=datetime.date.today()).count() + 1
        validated_data['order_number'] = f"ORD-{today}-{str(count).zfill(4)}"

        order = Order.objects.create(**validated_data)
        total = 0

        for item in items_data:
            product = item['product']
            item['unit_price'] = product.price
            order_item = OrderItem.objects.create(order=order, **item)
            total += order_item.line_total

        order.total_amount = total
        order.save()
        return order
    
    def update(self, instance, validated_data):
        if instance.status != 'DRAFT':
            raise serializers.ValidationError(
                "Only DRAFT orders can be modified"
            )
    
        items_data = validated_data.pop('items')
    
        instance.dealer = validated_data.get('dealer', instance.dealer)
        instance.save()
    
        # Existing items in DB
        existing_items = {
            item.id: item for item in instance.items.all()
        }
    
        received_item_ids = []
        total = 0
    
        for item_data in items_data:
            item_id = item_data.get('id')
            product = item_data['product']
            quantity = item_data['quantity']
            unit_price = product.price
    
            # 🔁 UPDATE EXISTING ITEM
            if item_id and item_id in existing_items:
                order_item = existing_items[item_id]
                order_item.product = product
                order_item.quantity = quantity
                order_item.unit_price = unit_price
                order_item.line_total = unit_price * quantity
                order_item.save()
                received_item_ids.append(item_id)
    
            # ➕ CREATE NEW ITEM
            else:
                order_item = OrderItem.objects.create(
                    order=instance,
                    product=product,
                    quantity=quantity,
                    unit_price=unit_price,
                    line_total=unit_price * quantity
                )
                received_item_ids.append(order_item.id)
    
            total += order_item.line_total
    
        # ❌ DELETE REMOVED ITEMS
        for item_id, item in existing_items.items():
            if item_id not in received_item_ids:
                item.delete()
    
        instance.total_amount = total
        instance.save()
    
        return instance
    
