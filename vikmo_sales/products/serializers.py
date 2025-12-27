from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # stock = serializers.IntegerField(
    #     source='inventory.quantity',
    #     read_only=True
    # )

    class Meta:
        model = Product
        fields = '__all__'
