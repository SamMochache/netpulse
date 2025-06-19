from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils import advanced_scan

class AdvancedScanView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'admin':
            return Response({'error': 'Access denied'}, status=403)

        subnet = request.query_params.get("subnet", "192.168.1.0/24")
        result = advanced_scan(subnet)
        return Response({"results": result})

