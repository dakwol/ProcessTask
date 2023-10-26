from rest_framework import serializers
from main_app.models import Process


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'


class ProcessDataSerializer(ProcessSerializer):
    class Meta:
        model = Process
        fields = ['client_value', 'input_data', 'output_data', 'related_processes']


class ProcessRetrieveSerializer(ProcessSerializer):
    data = ProcessDataSerializer(allow_null=True)

    class Meta:
        model = Process
        fields = ['id', 'name', 'status', 'is_internal_client', 'is_external_client', 'responsible_authority',
                  'department', 'is_digital_format', 'is_non_digital_format', 'digital_format_link', 'identifier',
                  'data']


class ProcessCreateSerializer(ProcessSerializer):
    class Meta:
        model = Process
        fields = ['name', 'service', 'status', 'is_internal_client', 'is_external_client', 'responsible_authority',
                  'department', 'is_digital_format', 'is_non_digital_format', 'digital_format_link', 'identifier']


class ProcessUpdateSerializer(ProcessSerializer):
    data = ProcessDataSerializer(allow_null=True)

    class Meta:
        model = Process
        fields = ['id', 'name', 'status', 'is_internal_client', 'is_external_client', 'responsible_authority', 'department',
                  'is_digital_format', 'is_non_digital_format', 'digital_format_link', 'data']
