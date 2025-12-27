from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
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
    
        # REMOVE old items
        instance.items.all().delete()
    
        total = 0
        for item in items_data:
            product = item['product']
            item['unit_price'] = product.price
            order_item = OrderItem.objects.create(order=instance, **item)
            total += order_item.line_total
    
        instance.total_amount = total
        instance.save()
    
        return instance
