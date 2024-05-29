from rest_framework import serializers

from testing.models import (Measurement, SpecificationGroup, Specification, Result,
                            NonCompliance, NonComplianceComment, Processor)


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'


class SpecificationGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationGroup
        fields = '__all__'


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class NonComplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonCompliance
        fields = '__all__'


class NonComplianceCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonComplianceComment
        fields = '__all__'


class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = '__all__'
