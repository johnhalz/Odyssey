from django.db import models


class UnitType(models.Model):
    name = models.CharField(max_length=30)


class Unit(models.Model):
    name = models.CharField(max_length=30)
    type_id = models.ForeignKey(UnitType, on_delete=models.CASCADE)
    base_unit_id = models.ForeignKey('self', on_delete=models.CASCADE)
    conversion_to_base = models.CharField(max_length=80, default="x")
    abbreviation = models.CharField(max_length=10)
