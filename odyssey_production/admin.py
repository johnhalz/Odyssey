from django.contrib import admin
from .value_models import Unit, UnitType, String, Integer, Decimal, Array, Value
from .value_models import HardwareModel, Hardware, Version, Order

# Register your models here.
admin.site.register(String)
admin.site.register(Integer)
admin.site.register(Decimal)
admin.site.register(Array)
admin.site.register(Value)

admin.site.register(Hardware)
admin.site.register(Version)


# Admin classes
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'type')
    search_fields = ('name', 'abbreviation')
    fields = ("name", "type", "base_unit", "abbreviation", "x_offset", "y_offset", "multiplicand", "denominator")
    ordering = ["name"]


@admin.register(UnitType)
class UnitTypeAdmin(admin.ModelAdmin):
    ordering = ["name"]


@admin.register(HardwareModel)
class HardwareModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'version')
    search_fields = ['name']
    fields = ("name", "position", "version")
    ordering = ["name"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'hardware', 'order_type')
    search_fields = ['number', 'hardware']
    fields = ("number", "hardware", "order_type")
    ordering = ["number"]
