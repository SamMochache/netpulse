from django.urls import path
from .views import TriggerScanView, ScanResultListView

urlpatterns = [
    path('trigger-scan/', TriggerScanView.as_view(), name='trigger-scan'),
    path('scan-results/', ScanResultListView.as_view(), name='scan-results'),
    

]
