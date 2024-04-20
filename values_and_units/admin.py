from django.contrib import admin
from .models import Unit, UnitType, String, Integer, Decimal, Array, Value, Version, Range

admin.site.register(UnitType)


# Admin classes
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'abbreviation', 'type')
    search_fields = ('id', 'name', 'abbreviation')
    fields = ("name", "type", "base_unit", "abbreviation", "x_offset", "y_offset", "multiplicand", "denominator")
    ordering = ["name"]


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'version', 'create_ts')
    search_fields = ('id', 'name')
    fields = ("name", 'major', 'minor', 'patch', 'create_ts')
    ordering = ["id"]


@admin.register(Range)
class RangeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lower', 'upper')
    search_fields = ('id', 'name')
    fields = ("name", 'lower', 'upper', 'create_ts')
    ordering = ["id"]


@admin.register(Integer)
class IntegerAdmin(admin.ModelAdmin):
    list_display = ('id', 'integer', 'unit', 'create_ts')
    search_fields = ('id', 'integer', 'unit')
    fields = ('integer', 'unit', 'create_ts')
    ordering = ["id"]


@admin.register(Decimal)
class DecimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'decimal', 'unit', 'create_ts')
    search_fields = ('id', 'decimal', 'unit')
    fields = ('decimal', 'unit', 'create_ts')
    ordering = ["id"]


@admin.register(Array)
class ArrayAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_count', 'unit', 'create_ts')
    search_fields = ('id', 'unit')
    fields = ('array', 'unit', 'create_ts')
    ordering = ["id"]


@admin.register(String)
class StringAdmin(admin.ModelAdmin):
    list_display = ('id', 'string', 'create_ts')
    search_fields = ('id', 'string')
    fields = ('string', 'create_ts')
    ordering = ["id"]


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_object')
    search_fields = ('id', 'content_object')
    fields = ['object_id']
    ordering = ["id"]

    def has_add_permission(self, request):
        return False
