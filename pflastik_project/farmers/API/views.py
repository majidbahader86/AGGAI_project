# farmers/api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import (
    MonitoringData,
    MonitoringAlert,
    MonitoringAction,
    ForumPost,
    ForumComment,
    SeasonAlert,
    EnvironmentalCondition,
    CareTip,
    FinancialAid
)
from .serializers import (
    MonitoringDataSerializer,
    MonitoringAlertSerializer,
    MonitoringActionSerializer,
    ForumPostSerializer,
    ForumCommentSerializer,
    SeasonAlertSerializer,
    EnvironmentalConditionSerializer,
    CareTipSerializer,
    FinancialAidSerializer
)

class MonitoringDataListCreateView(generics.ListCreateAPIView):
    queryset = MonitoringData.objects.all()
    serializer_class = MonitoringDataSerializer
    permission_classes = [IsAuthenticated]

class MonitoringDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonitoringData.objects.all()
    serializer_class = MonitoringDataSerializer
    permission_classes = [IsAuthenticated]

class MonitoringAlertListCreateView(generics.ListCreateAPIView):
    queryset = MonitoringAlert.objects.all()
    serializer_class = MonitoringAlertSerializer
    permission_classes = [IsAuthenticated]

class MonitoringAlertDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonitoringAlert.objects.all()
    serializer_class = MonitoringAlertSerializer
    permission_classes = [IsAuthenticated]

class MonitoringActionListCreateView(generics.ListCreateAPIView):
    queryset = MonitoringAction.objects.all()
    serializer_class = MonitoringActionSerializer
    permission_classes = [IsAuthenticated]

class MonitoringActionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonitoringAction.objects.all()
    serializer_class = MonitoringActionSerializer
    permission_classes = [IsAuthenticated]

class ForumPostListCreateView(generics.ListCreateAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = [IsAuthenticated]

class ForumPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = [IsAuthenticated]

class ForumCommentListCreateView(generics.ListCreateAPIView):
    queryset = ForumComment.objects.all()
    serializer_class = ForumCommentSerializer
    permission_classes = [IsAuthenticated]

class ForumCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumComment.objects.all()
    serializer_class = ForumCommentSerializer
    permission_classes = [IsAuthenticated]

class SeasonAlertListCreateView(generics.ListCreateAPIView):
    queryset = SeasonAlert.objects.all()
    serializer_class = SeasonAlertSerializer
    permission_classes = [IsAuthenticated]

class SeasonAlertDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SeasonAlert.objects.all()
    serializer_class = SeasonAlertSerializer
    permission_classes = [IsAuthenticated]

class EnvironmentalConditionListCreateView(generics.ListCreateAPIView):
    queryset = EnvironmentalCondition.objects.all()
    serializer_class = EnvironmentalConditionSerializer
    permission_classes = [IsAuthenticated]

class EnvironmentalConditionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnvironmentalCondition.objects.all()
    serializer_class = EnvironmentalConditionSerializer
    permission_classes = [IsAuthenticated]

class CareTipListCreateView(generics.ListCreateAPIView):
    queryset = CareTip.objects.all()
    serializer_class = CareTipSerializer
    permission_classes = [IsAuthenticated]

class CareTipDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CareTip.objects.all()
    serializer_class = CareTipSerializer
    permission_classes = [IsAuthenticated]

class FinancialAidListCreateView(generics.ListCreateAPIView):
    queryset = FinancialAid.objects.all()
    serializer_class = FinancialAidSerializer
    permission_classes = [IsAuthenticated]

class FinancialAidDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FinancialAid.objects.all()
    serializer_class = FinancialAidSerializer
    permission_classes = [IsAuthenticated]