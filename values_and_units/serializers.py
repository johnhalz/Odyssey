from rest_framework import serializers

from values_and_units.models import UnitType, Unit, String, Integer, Decimal, Array, Value, Version, Range


class UnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitType
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class StringSerializer(serializers.ModelSerializer):
    class Meta:
        model = String
        fields = '__all__'


class IntegerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integer
        fields = '__all__'


class DecimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decimal
        fields = '__all__'


class ArraySerializer(serializers.ModelSerializer):
    class Meta:
        model = Array
        fields = '__all__'


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = '__all__'


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'


class RangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Range
        fields = '__all__'
