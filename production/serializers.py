from rest_framework import serializers

from production.models import ProductionStepModel, Configuration, ProductionStep


class ProductionStepModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionStepModel
        fields = ['id', 'name', 'parent', 'hardware_model', 'equipment',
                  'version', 'step_number', 'optional', 'create_ts']


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ['id', 'name', 'parent', 'value', 'hardware_model', 'production_step_model',
                  'version', 'description', 'create_ts']


class ProductionStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionStep
        fields = ['id', 'order', 'production_step_model', 'status', 'operator', 'start_ts', 'end_ts']
