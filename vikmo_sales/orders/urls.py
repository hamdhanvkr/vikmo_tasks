from django.urls import path
from .views import (
    OrderListCreateAPIView,
    OrderDetailAPIView,
    OrderConfirmAPIView,
    OrderDeliverAPIView
)

urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view()),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view()),
    path('orders/<int:pk>/confirm/', OrderConfirmAPIView.as_view()),
    path('orders/<int:pk>/deliver/', OrderDeliverAPIView.as_view()),
]
