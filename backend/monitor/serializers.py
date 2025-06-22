# backend/monitor/serializers.py
from rest_framework import serializers
from .models import ScanResult, User

class ScanResultSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = ScanResult
        fields = ['id', 'username', 'subnet', 'results', 'timestamp']
        read_only_fields = ['id', 'username', 'timestamp']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
        read_only_fields = ['id']