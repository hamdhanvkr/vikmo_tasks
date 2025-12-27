from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id', read_only=True)
    sku = serializers.CharField(source='product.sku', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Inventory
        fields = [
            'product_id',
            'sku',
            'product_name',
            'quantity',
            'updated_by',
            'updated_at'
        ]
