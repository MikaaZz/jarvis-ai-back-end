from rest_framework import viewsets
from .models import UserRequest, APIResponse
from .serializers import UserRequestSerializer, APIResponseSerializer
import openai


class UserRequestViewSet(viewsets.ModelViewSet):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=instance.prompt,
          max_tokens=100
        )

        APIResponse.objects.create(
            user_request=instance,
            response_text=response.choices[0].text.strip(),
        )

class APIResponseViewSet(viewsets.ModelViewSet):
    queryset = APIResponse.objects.all()
    serializer_class = APIResponseSerializer
