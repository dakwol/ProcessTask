from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import LifeSituation
from .serializers.life_situation_serializers import LifeSituationGetSerializer, LifeSituationCreateSerializer, \
    LifeSituationUpdateSerializer, LifeSituationSerializer
from .utils import CustomOptionsMetadata, generate_identifier


class LifeSituationViewSet(viewsets.ModelViewSet):
    queryset = LifeSituation.objects.all()
    metadata_class = CustomOptionsMetadata
    serializer_class = LifeSituationSerializer
    serializer_list = {
        'get': LifeSituationGetSerializer,
        'create': LifeSituationCreateSerializer,
        'update': LifeSituationUpdateSerializer,
    }
    #permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def generate_identifier(self, request):
        identifier = generate_identifier()
        return Response({'identifier': identifier}, status=status.HTTP_200_OK)