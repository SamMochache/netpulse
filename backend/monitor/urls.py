from django.urls import path
from .views import AdvancedScanView

urlpatterns = [
    path('scan/', AdvancedScanView.as_view(), name='advanced-scan'),
]
