from rest_framework import serializers
from .models import UserRequest, APIResponse

class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = ['id', 'timestamp', 'prompt']

class APIResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIResponse
        fields = ['id', 'timestamp', 'user_request', 'response_text']
