from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .units import Unit


class String(models.Model):
    string = models.CharField(max_length=100)

    def __str__(self):
        return self.string


class Integer(models.Model):
    integer = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)

    def __str__(self):
        string_value = str(self.integer)
        if self.unit is not None:
            string_value += f" {self.unit.abbreviation}"

        return string_value


class Decimal(models.Model):
    decimal = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)

    def __str__(self):
        string_value = str(self.decimal)
        if self.unit is not None:
            string_value += f" {self.unit.abbreviation}"

        return string_value


class Array(models.Model):
    array = ArrayField(models.FloatField())
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)

    def __str__(self):
        string_value = str(self.array)
        if self.unit is not None:
            string_value += f" {self.unit}"

        return string_value


class Value(models.Model):
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.name}: {self.content_object}"
