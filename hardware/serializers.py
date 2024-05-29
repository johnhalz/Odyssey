from rest_framework import serializers

from hardware.models import Hardware, HardwareModel, Order, Equipment


class HardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hardware
        fields = ['id', 'serial_number', 'set', 'create_ts', 'model']


class HardwareModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardwareModel
        fields = ['id', 'position', 'parent', 'version', 'create_ts']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'number', 'hardware', 'order_type', 'create_ts']


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'number', 'calibration_ts', 'parent', 'status', 'create_ts']
