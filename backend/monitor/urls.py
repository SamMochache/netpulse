from django.urls import path
from .views import TriggerScanView

urlpatterns = [
    path('trigger-scan/', TriggerScanView.as_view(), name='trigger-scan'),

]
