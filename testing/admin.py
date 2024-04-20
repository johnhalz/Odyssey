from django.contrib import admin
from .models import Measurement, SpecificationGroup, Specification, Result, NonCompliance, NonComplianceComment


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'create_ts', 'production_step')
    search_fields = ('id', 'name')
    fields = ("name", "value", "create_ts", "production_step")
    ordering = ["id"]


@admin.register(SpecificationGroup)
class SpecificationGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'commencement_date', 'expiration_date')
    search_fields = ('id', 'name')
    fields = ("name", "commencement_date", "expiration_date")
    ordering = ["id"]


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'valid_range', 'applicable_scope', 'hardware_model', 'production_step',
                    'group', 'severity', 'version')
    search_fields = ('id', 'name', 'group', 'severity')
    fields = ("name", "valid_range", "applicable_scope", "hardware_model", "production_step", "group", "severity",
              "version")
    ordering = ["id"]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'name', 'value', 'create_ts', 'processor_name', 'processor_version')
    search_fields = ('id', 'name', 'processor_name')
    fields = ("name", "create_ts", "parent", "value", "processor_name", "processor_version", "measurements",
              "specifications")
    ordering = ["id"]


@admin.register(NonCompliance)
class NonComplianceAdmin(admin.ModelAdmin):
    list_display = ('id', 'result', 'status', 'reporter', 'create_ts')
    search_fields = ('id', 'status', 'reporter')
    fields = ('create_ts', 'result', 'status', 'reporter', 'decision', 'signer')
    ordering = ["id"]


@admin.register(NonComplianceComment)
class NonComplianceCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_ts', 'parent', 'non_compliance', 'author')
    search_fields = ('id', 'non_compliance', 'author')
    fields = ('create_ts', 'parent', 'non_compliance', 'author', 'content')
    ordering = ["id"]
