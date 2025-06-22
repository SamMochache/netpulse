# backend/monitor/tasks.py
from celery import shared_task
from .utils import advanced_scan
from .models import ScanResult, User
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def run_network_scan(self, subnet, user_id):
    """
    Celery task to run network scan
    """
    try:
        logger.info(f"Starting network scan for subnet: {subnet}")
        
        # Run the actual scan
        result = advanced_scan(subnet)
        
        # Get user and save results
        user = User.objects.get(id=user_id)
        scan_result = ScanResult.objects.create(
            user=user, 
            subnet=subnet, 
            results=result
        )
        
        logger.info(f"Scan completed successfully. Found {len(result)} hosts. Saved as scan result ID: {scan_result.id}")
        
        return {
            "status": "completed",
            "scan_id": scan_result.id,
            "hosts_found": len(result),
            "hosts": result
        }
        
    except User.DoesNotExist:
        logger.error(f"User with ID {user_id} not found")
        return {"status": "failed", "error": "User not found"}
        
    except Exception as e:
        logger.error(f"Network scan failed: {str(e)}")
        return {"status": "failed", "error": str(e)}

# ============================================