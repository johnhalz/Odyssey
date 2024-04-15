from django.db import models


class UnitType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Unit(models.Model):
    name = models.CharField(max_length=30)
    plural_name = models.CharField(max_length=30, blank=True, null=True)
    space_after_value = models.BooleanField(default=True)
    type = models.ForeignKey(UnitType, on_delete=models.CASCADE)
    base_unit = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    abbreviation = models.CharField(max_length=10)
    """
    For conversion, we will use the formula:
    y = ((x + x_offset) * multiplicand / denominator) + y_offset
    
    We create the fields to store these constants
    """
    x_offset = models.DecimalField(max_digits=19, decimal_places=10, default=0)
    y_offset = models.DecimalField(max_digits=19, decimal_places=10, default=0)
    multiplicand = models.DecimalField(max_digits=19, decimal_places=10, default=1)
    denominator = models.DecimalField(max_digits=19, decimal_places=10, default=1)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"
