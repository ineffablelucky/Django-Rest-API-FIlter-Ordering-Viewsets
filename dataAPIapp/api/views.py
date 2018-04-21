from .serializers import UserProfileSerializer
from dataAPIapp.models import UserProfile
from rest_framework import viewsets
from django.db.models import Q
import django_filters
from rest_framework.filters import OrderingFilter

class UserAPIView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        name_search = self.request.query_params.get("name", None)
        if name_search is not None:
            queryset = queryset.filter(Q(first_name__icontains=name_search)
                                    | Q(last_name__icontains=name_search))


        return queryset
