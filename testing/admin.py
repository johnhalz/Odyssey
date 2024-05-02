from django.contrib import admin
from .models import Measurement, SpecificationGroup, Specification, Result, NonCompliance, NonComplianceComment, Processor


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'create_ts', 'production_step')
    search_fields = ('id', 'name')
    fields = ("name", "value", "create_ts", "production_step")
    ordering = ["id"]


@admin.register(SpecificationGroup)
class SpecificationGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'commencement_date', 'expiration_date', 'create_ts')
    search_fields = ('id', 'name')
    fields = ("name", "commencement_date", "expiration_date", 'create_ts')
    ordering = ["id"]


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'valid_range', 'applicable_scope', 'hardware_model', 'production_step_model',
                    'group', 'severity', 'version', 'create_ts')
    search_fields = ('id', 'name', 'group', 'severity')
    fields = ("name", "valid_range", "applicable_scope", "hardware_model", "production_step_model", "group", "severity",
              "version", 'create_ts')
    ordering = ["id"]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'name', 'value', 'create_ts', 'processor')
    search_fields = ('id', 'name', 'processor_name')
    fields = ("name", "create_ts", "parent", "value", "processor", "measurements", "specifications")
    ordering = ["id"]


@admin.register(NonCompliance)
class NonComplianceAdmin(admin.ModelAdmin):
    list_display = ('id', 'result', 'status', 'reporter', 'create_ts', 'close_ts')
    search_fields = ('id', 'status', 'reporter')
    fields = ('create_ts', 'close_ts', 'result', 'status', 'reporter', 'decision', 'signer')
    ordering = ["id"]


@admin.register(NonComplianceComment)
class NonComplianceCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_ts', 'parent', 'non_compliance', 'author')
    search_fields = ('id', 'non_compliance', 'author')
    fields = ('create_ts', 'parent', 'non_compliance', 'author', 'content')
    ordering = ["id"]


@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_ts', 'version')
    search_fields = ('id', 'name')
    fields = ('name', 'create_ts', 'version', 'file_path')
    ordering = ["id"]
