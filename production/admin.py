from django.contrib import admin
from .models import ProductionStepModel, ProductionStep, Configuration


@admin.register(ProductionStepModel)
class ProductionStepModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hardware_model', 'version', 'step_number', 'optional')
    search_fields = ['id', 'name']
    fields = ['name', 'parent', 'hardware_model', 'equipment', 'version', 'step_number', 'optional']
    ordering = ["id"]


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'hardware_model', 'production_step_model', 'version')
    search_fields = ['id', 'name']
    fields = ['name', 'value', 'hardware_model', 'production_step_model', 'version', 'description']
    ordering = ["id"]


@admin.register(ProductionStep)
class ProductionStepAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'status', 'operator', 'start_timestamp', 'end_timestamp')
    search_fields = ['id', 'order', 'production_step_model']
    fields = ['order', 'status', 'operator', 'start_timestamp', 'end_timestamp']
    ordering = ["id"]
