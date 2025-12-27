from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from .models import Order
from .serializers import OrderSerializer
from .services import confirm_order, deliver_order

class OrderListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        orders = Order.objects.all()
        return Response(OrderSerializer(orders, many=True).data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(OrderSerializer(order).data, status=201)
        return Response(serializer.errors, status=400)


class OrderDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        return Response(OrderSerializer(order).data)

    def put(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class OrderConfirmAPIView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, pk):
        order = get_object_or_404(Order, pk=pk)

        try:
            confirm_order(order)
            order.refresh_from_db() 
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": e.args[0]},
                status=status.HTTP_400_BAD_REQUEST
            )


class OrderDeliverAPIView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, pk):
        order = get_object_or_404(Order, pk=pk)

        try:
            deliver_order(order)
            order.refresh_from_db() 
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )