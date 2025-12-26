from rest_framework import serializers
from .models import OrderItem
from products.models import Product
from .models import Order
from django.db import transaction
from inventory.models import Inventory

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'unit_price', 'line_total']
        read_only_fields = ['line_total']



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['order_number', 'total_amount']

    def validate(self, data):
        if self.instance and self.instance.status != 'DRAFT':
            raise serializers.ValidationError(
                "Only DRAFT orders can be modified"
            )
        return data