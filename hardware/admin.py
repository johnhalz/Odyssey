from django.contrib import admin
from .models import HardwareModel, Hardware, Order, Equipment

admin.site.register(Hardware)


@admin.register(HardwareModel)
class HardwareModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'version')
    search_fields = ['id', 'name']
    fields = ("name", "position", "version")
    ordering = ["id"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'hardware', 'order_type')
    search_fields = ['number', 'hardware']
    fields = ("number", "hardware", "order_type")
    ordering = ["number"]


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'calibration_ts', 'status')
    search_fields = ['name']
    fields = ("name", "number", "calibration_ts", "parent", "status")
    ordering = ["name"]
