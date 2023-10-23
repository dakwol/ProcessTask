from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import LifeSituation, Service, Process
from .serializers.life_situation_serializers import LifeSituationRetrieveSerializer, LifeSituationCreateSerializer, \
    LifeSituationUpdateSerializer, LifeSituationSerializer, LifeSituationListSerializer
from .serializers.process_serializers import ProcessSerializer, ProcessRetrieveSerializer, ProcessCreateSerializer, \
    ProcessUpdateSerializer
from .serializers.service_serializers import ServiceSerializer, ServiceRetrieveSerializer, ServiceCreateSerializer, \
    ServiceUpdateSerializer
from .utils import generate_identifier, CustomModelViewSet


class LifeSituationViewSet(CustomModelViewSet):
    queryset = LifeSituation.objects.all()
    serializer_class = LifeSituationSerializer
    serializer_list = {
        'list': LifeSituationListSerializer,
        'retrieve': LifeSituationRetrieveSerializer,
        'create': LifeSituationCreateSerializer,
        'update': LifeSituationUpdateSerializer,
    }
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = LifeSituation.objects.filter(user=user)
        return queryset

    @action(detail=False, methods=['get'])
    def generate_identifier(self, request):
        identifier = generate_identifier()
        return Response({'identifier': identifier}, status=status.HTTP_200_OK)


class ServiceViewSet(CustomModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    serializer_list = {
        'list': ServiceRetrieveSerializer,
        'retrieve': ServiceRetrieveSerializer,
        'create': ServiceCreateSerializer,
        'update': ServiceUpdateSerializer,
    }
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = LifeSituation.objects.filter(user=user)
        return queryset


class ProcessViewSet(CustomModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    serializer_list = {
        'list': ProcessRetrieveSerializer,
        'retrieve': ProcessRetrieveSerializer,
        'create': ProcessCreateSerializer,
        'update': ProcessUpdateSerializer,
    }
    #permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def generate_identifier(self, request):
        identifier = generate_identifier()
        return Response({'identifier': identifier}, status=status.HTTP_200_OK)
