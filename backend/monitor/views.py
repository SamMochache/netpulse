from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .tasks import run_network_scan

class TriggerScanView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != 'analyst':
            return Response({'error': 'Unauthorized'}, status=403)

        subnet = request.data.get("subnet", "192.168.1.0/24")
        task = run_network_scan.delay(subnet)
        return Response({"task_id": task.id})

