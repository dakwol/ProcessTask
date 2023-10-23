from rest_framework import serializers
from main_app.models import LifeSituation
from main_app.serializers.service_serializers import ServiceRetrieveSerializer


class LifeSituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeSituation
        fields = '__all__'


class LifeSituationListSerializer(LifeSituationSerializer):
    services = ServiceRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = LifeSituation
        fields = ['id', 'name', 'identifier', 'services']


class LifeSituationRetrieveSerializer(LifeSituationSerializer):
    class Meta:
        model = LifeSituation
        fields = ['id', 'name', 'identifier']


class LifeSituationCreateSerializer(LifeSituationSerializer):
    class Meta:
        model = LifeSituation
        fields = ['name', 'identifier']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return LifeSituation.objects.create(**validated_data)


class LifeSituationUpdateSerializer(LifeSituationSerializer):
    class Meta:
        model = LifeSituation
        fields = ['id', 'name']
