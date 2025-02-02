from rest_framework import serializers
from main_app.models import Service
from main_app.serializers.process_serializers import ProcessRetrieveSerializer


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceListSerializer(ServiceSerializer):
    processes = ProcessRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'service_type', 'name', 'regulating_act', 'processes']


class ServiceRetrieveSerializer(ServiceSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_type', 'name', 'regulating_act']


class ServiceCreateSerializer(ServiceSerializer):
    class Meta:
        model = Service
        fields = ['service_type', 'name', 'regulating_act', 'lifesituation']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return Service.objects.create(**validated_data)


class ServiceUpdateSerializer(ServiceSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_type', 'name', 'regulating_act']
