from django.contrib import admin
from .models import HardwareModel, Hardware, Order, Equipment


@admin.register(Hardware)
class HardwareAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'model', 'set', 'create_ts')
    search_fields = ['id', 'serial_number']
    fields = ("name", 'serial_number', 'model', 'set', 'create_ts')
    ordering = ["id"]


@admin.register(HardwareModel)
class HardwareModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'version', 'create_ts')
    search_fields = ['id', 'name']
    fields = ("name", "position", "version", 'create_ts')
    ordering = ["id"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'hardware', 'order_type', 'create_ts')
    search_fields = ['number', 'hardware']
    fields = ("number", "hardware", "order_type", 'create_ts')
    ordering = ["number"]


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'calibration_ts', 'status', 'create_ts')
    search_fields = ['name']
    fields = ("name", "number", "calibration_ts", "parent", "status", 'create_ts')
    ordering = ["name"]
