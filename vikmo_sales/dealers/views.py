from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dealer
from .serializers import DealerSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny

# ---------------- List / Create Dealers ----------------
class DealerListCreateAPIView(APIView):
    permission_classes = [AllowAny]  # allows public access

    def get(self, request):
        dealers = Dealer.objects.all()
        serializer = DealerSerializer(dealers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DealerSerializer(data=request.data)
        if serializer.is_valid():
            dealer = serializer.save()
            return Response(DealerSerializer(dealer).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------------- Retrieve / Update / Delete Dealer ----------------
class DealerDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        dealer = get_object_or_404(Dealer, pk=pk)
        serializer = DealerSerializer(dealer)
        return Response(serializer.data)

    def put(self, request, pk):
        dealer = get_object_or_404(Dealer, pk=pk)
        serializer = DealerSerializer(dealer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dealer = get_object_or_404(Dealer, pk=pk)
        dealer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
