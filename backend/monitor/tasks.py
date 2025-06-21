# tasks.py
from celery import shared_task
from .utils import advanced_scan
from .models import ScanResult, User

@shared_task
def run_network_scan(subnet, user_id):
    result = advanced_scan(subnet)
    user = User.objects.get(id=user_id)
    ScanResult.objects.create(user=user, subnet=subnet, results=result)
    return {"status": "saved", "hosts": result}
