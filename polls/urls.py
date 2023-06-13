from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRequestViewSet, APIResponseViewSet

router = DefaultRouter()
router.register(r'user-requests', UserRequestViewSet)
router.register(r'api-responses', APIResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
