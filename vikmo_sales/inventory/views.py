from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Inventory
from .serializers import InventorySerializer
from products.models import Product


class InventoryListAPIView(APIView):
    permission_classes = [ IsAuthenticated]

    def get(self, request):
        inventory = Inventory.objects.select_related('product').all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)


class InventoryUpdateAPIView(APIView):
    permission_classes =[ IsAuthenticated]

    def put(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        inventory, created = Inventory.objects.get_or_create(product=product)

        quantity = request.data.get('quantity')
        if quantity is None:
            return Response(
                {"error": "quantity is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        inventory.quantity = quantity
        inventory.updated_by = request.user.username
        inventory.save()

        serializer = InventorySerializer(inventory)
        return Response(serializer.data, status=status.HTTP_200_OK)
