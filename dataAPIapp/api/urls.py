from django.urls import path, include
from dataAPIapp.api.views import UserAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserAPIView,'users')

urlpatterns = [
    path('', include(router.urls)),
]
