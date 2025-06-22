# backend/monitor/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from .tasks import run_network_scan
from .models import ScanResult
from .serializers import ScanResultSerializer
import logging

logger = logging.getLogger(__name__)
User = get_user_model()

class TriggerScanView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Check if user has admin role
        if not hasattr(request.user, 'role') or request.user.role != 'admin':
            logger.warning(f"Unauthorized scan attempt by user: {request.user.username}")
            return Response(
                {'error': 'Only admin users can trigger scans'}, 
                status=status.HTTP_403_FORBIDDEN
            )

        subnet = request.data.get("subnet", "192.168.1.0/24")
        
        # Validate subnet format (basic validation)
        if not subnet or not isinstance(subnet, str):
            return Response(
                {'error': 'Invalid subnet format'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Start the Celery task
            task = run_network_scan.delay(subnet, request.user.id)
            logger.info(f"Started network scan task {task.id} for subnet {subnet} by user {request.user.username}")
            
            return Response({
                "task_id": task.id,
                "subnet": subnet,
                "status": "started"
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            logger.error(f"Failed to start scan task: {str(e)}")
            return Response(
                {'error': 'Failed to start scan task'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ScanResultListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Get scan results for the authenticated user
            scans = ScanResult.objects.filter(user=request.user).order_by('-timestamp')
            serializer = ScanResultSerializer(scans, many=True)
            
            logger.info(f"Retrieved {len(serializer.data)} scan results for user {request.user.username}")
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Failed to retrieve scan results: {str(e)}")
            return Response(
                {'error': 'Failed to retrieve scan results'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'username': request.user.username,
            'role': getattr(request.user, 'role', 'analyst'),
            'email': request.user.email,
        })

# ============================================