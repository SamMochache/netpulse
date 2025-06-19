from celery import shared_task
from .utils import advanced_scan

@shared_task
def run_network_scan(subnet):
    result = advanced_scan(subnet)
    return result
