from django.db import models
from django.utils import timezone


class Hardware(models.Model):
    serial_number = models.CharField(max_length=255)
    model = models.ForeignKey('HardwareModel', related_name='hardware_models', on_delete=models.DO_NOTHING)
    set = models.PositiveIntegerField(default=1)
    create_ts = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Hardware'


class HardwareModel(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True, default=None)
    version = models.ForeignKey('values_and_units.Version', null=True, blank=True, on_delete=models.CASCADE)
    create_ts = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Hardware Models'

    def __str__(self):
        return f"{self.name} ({self.position}) - {self.version}"


class Order(models.Model):
    number = models.PositiveIntegerField(unique=True)
    hardware = models.ForeignKey('Hardware', related_name='orders', on_delete=models.CASCADE)
    order_type = models.CharField(max_length=255)
    create_ts = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.number} - {self.order_type}"


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    number = models.PositiveIntegerField(unique=True, default=1)
    calibration_ts = models.DateTimeField()
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True, default=None)
    status = models.CharField(max_length=255)
    create_ts = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Equipment'

    def __str__(self):
        return f"{self.name} (#{self.number})"
