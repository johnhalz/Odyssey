from django.contrib import admin
from .models import ProductionStepModel, ProductionStep, Configuration


@admin.register(ProductionStepModel)
class ProductionStepModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hardware_model', 'version', 'step_number', 'optional', 'create_ts')
    search_fields = ['id', 'name']
    fields = ['name', 'parent', 'hardware_model', 'equipment', 'version', 'step_number', 'optional']
    ordering = ["id"]


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'parent', 'hardware_model', 'production_step_model', 'version', 'create_ts')
    search_fields = ['id', 'name']
    fields = ['parent', 'name', 'value', 'hardware_model', 'production_step_model', 'version', 'description', 'create_ts']
    ordering = ["id"]


@admin.register(ProductionStep)
class ProductionStepAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'status', 'operator', 'start_ts', 'end_ts')
    search_fields = ['id', 'order', 'production_step_model']
    fields = ['order', 'status', 'operator', 'start_ts', 'end_ts']
    ordering = ["id"]
