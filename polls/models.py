from django.db import models

# Create your models here.
class UserRequest(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    prompt = models.TextField()

    def __str__(self):
        return self.prompt

class APIResponse(models.Model):
    user_request = models.ForeignKey(UserRequest, on_delete=models.CASCADE, related_name='responses')
    timestamp = models.DateTimeField(auto_now_add=True)
    response_text = models.TextField()

    def __str__(self):
        return self.response_text
