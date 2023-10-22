from rest_framework import serializers
from main_app.models import LifeSituation


class LifeSituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeSituation
        fields = ['id', 'name', 'identifier']


class LifeSituationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeSituation
        fields = ['id', 'name', 'identifier']


class LifeSituationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeSituation
        fields = ['name', 'identifier']


class LifeSituationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeSituation
        fields = ['id', 'name']
