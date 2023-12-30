from django.contrib import admin
from .value_models import Unit, UnitType, String, Integer, Decimal, Array, Value

# Register your models here.
admin.site.register(Unit)
admin.site.register(UnitType)
admin.site.register(String)
admin.site.register(Integer)
admin.site.register(Decimal)
admin.site.register(Array)
admin.site.register(Value)
