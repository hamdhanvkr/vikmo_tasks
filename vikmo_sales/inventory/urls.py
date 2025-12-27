from django.urls import path
from .views import InventoryListAPIView, InventoryUpdateAPIView

urlpatterns = [
    path('inventory/', InventoryListAPIView.as_view()),
    path('inventory/<int:product_id>/', InventoryUpdateAPIView.as_view()),
]
