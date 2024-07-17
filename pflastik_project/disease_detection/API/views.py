from rest_framework import viewsets
from rest_framework import permissions
from ..models import DiseaseIdentificationRequest
from .serializers import DiseaseIdentificationRequestSerializer

class DiseaseIdentificationRequestViewSet(viewsets.ModelViewSet):
    queryset = DiseaseIdentificationRequest.objects.all()
    serializer_class = DiseaseIdentificationRequestSerializer
    permission_classes = [permissions.IsAuthenticated]