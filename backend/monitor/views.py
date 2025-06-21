# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .tasks import run_network_scan
from .models import ScanResult
from .serializers import ScanResultSerializer

class TriggerScanView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != 'admin':
            return Response({'error': 'Unauthorized'}, status=403)

        subnet = request.data.get("subnet", "192.168.1.0/24")
        task = run_network_scan.delay(subnet, request.user.id)
        return Response({"task_id": task.id})


class ScanResultListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        scans = ScanResult.objects.filter(user=request.user).order_by('-timestamp')
        serializer = ScanResultSerializer(scans, many=True)
        return Response(serializer.data)
