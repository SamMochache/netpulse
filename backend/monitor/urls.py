# backend/monitor/urls.py
from django.urls import path
from .views import TriggerScanView, ScanResultListView, UserProfileView

app_name = 'monitor'

urlpatterns = [
    path('trigger-scan/', TriggerScanView.as_view(), name='trigger-scan'),
    path('scan-results/', ScanResultListView.as_view(), name='scan-results'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]

# ============================================