from django.urls import path
from .views import DealerListCreateAPIView, DealerDetailAPIView

urlpatterns = [
    path('dealers/', DealerListCreateAPIView.as_view(), name='dealer_list_create'),
    path('dealers/<int:pk>/', DealerDetailAPIView.as_view(), name='dealer_detail'),
]
