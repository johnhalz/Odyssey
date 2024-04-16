from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class UnitType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Unit Types'


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


class String(models.Model):
    string = models.CharField(max_length=100)
    create_ts = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.string


class Integer(models.Model):
    integer = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)
    create_ts = models.DateTimeField(default=timezone.now)

    def __str__(self):
        string_value = str(self.integer)
        if self.unit is not None:
            string_value += f" {self.unit.abbreviation}"

        return string_value


class Decimal(models.Model):
    decimal = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)
    create_ts = models.DateTimeField(default=timezone.now)

    def __str__(self):
        string_value = str(self.decimal)
        if self.unit is not None:
            string_value += f" {self.unit.abbreviation}"

        return string_value


class Array(models.Model):
    array = ArrayField(models.FloatField())
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)
    create_ts = models.DateTimeField(default=timezone.now)

    def __str__(self):
        string_value = str(self.array)
        if self.unit is not None:
            string_value += f" {self.unit}"

        return string_value

    def item_count(self):
        return f"{len(self.array)} items"


class Value(models.Model):
    INTEGER = 'integer'
    DECIMAL = 'decimal'
    ARRAY = 'array'
    STRING = 'string'

    VALUE_TYPES = [
        (INTEGER, 'Integer'),
        (DECIMAL, 'Decimal'),
        (ARRAY, 'Array'),
        (STRING, 'String'),
    ]

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('integer', 'decimal', 'array', 'string')}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)
    create_ts = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.content_object}"


class Version(models.Model):
    name = models.CharField(max_length=255)
    major = models.IntegerField(default=1)
    minor = models.IntegerField(default=0)
    patch = models.IntegerField(default=0)
    create_ts = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} v{self.major}.{self.minor}.{self.patch}"

    def version(self):
        return f"{self.major}.{self.minor}.{self.patch}"


class Range(models.Model):
    name = models.CharField(max_length=255)
    lower = models.ForeignKey('Value', on_delete=models.DO_NOTHING, related_name='lower_ranges', default=None)
    upper = models.ForeignKey('Value', on_delete=models.DO_NOTHING, related_name='upper_ranges', default=None)
    create_ts = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.lower}..{self.upper})"
