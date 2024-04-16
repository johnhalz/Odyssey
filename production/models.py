from django.db import models
from django.contrib.auth.models import User


class ProductionStepModel(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('ProductionStepModel', related_name='children', on_delete=models.CASCADE, null=True, blank=True, default=None)
    hardware_model = models.ForeignKey('hardware.HardwareModel', related_name='production_step_models', on_delete=models.DO_NOTHING)
    equipment = models.ForeignKey('hardware.Equipment', related_name='production_step_models', on_delete=models.DO_NOTHING)
    version = models.ForeignKey('values_and_units.Version', related_name='production_step_models', on_delete=models.CASCADE)
    step_number = models.IntegerField(default=0)
    optional = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.version})"


class Configuration(models.Model):
    name = models.CharField(max_length=100)
    value = models.ForeignKey('values_and_units.Value', related_name='configurations', on_delete=models.CASCADE)
    hardware_model = models.ForeignKey('hardware.HardwareModel', related_name='configurations', on_delete=models.DO_NOTHING)
    production_step_model = models.ForeignKey('ProductionStepModel', related_name='configurations', on_delete=models.DO_NOTHING)
    version = models.ForeignKey('values_and_units.Version', related_name='configurations', on_delete=models.CASCADE)
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.name} ({self.version})"


class ProductionStep(models.Model):
    order = models.ForeignKey('hardware.Order', related_name='production_steps', on_delete=models.DO_NOTHING)
    production_step_model = models.ForeignKey('ProductionStepModel', related_name='production_steps', on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=255)
    operator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='executed_production_steps')
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.order
