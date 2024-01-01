from django.db import models


class UnitType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Unit(models.Model):
    name = models.CharField(max_length=30)
    type = models.ForeignKey(UnitType, on_delete=models.CASCADE)
    base_unit = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    conversion_to_base = models.CharField(max_length=80, default="x")
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"
