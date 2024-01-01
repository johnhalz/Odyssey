from django.contrib import admin
from .value_models import Unit, UnitType, String, Integer, Decimal, Array, Value

# Register your models here.
# admin.site.register(UnitType)
admin.site.register(String)
admin.site.register(Integer)
admin.site.register(Decimal)
admin.site.register(Array)
admin.site.register(Value)


# Admin classes
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'type', 'base_unit')
    search_fields = ('name', 'abbreviation')
    fields = ("name", "type", "base_unit", "conversion_to_base", "abbreviation")
    ordering = ["name"]


@admin.register(UnitType)
class UnitTypeAdmin(admin.ModelAdmin):
    ordering = ["name"]
