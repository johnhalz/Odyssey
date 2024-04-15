from django.db import models


class Hardware(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    model = models.ForeignKey('HardwareModel', related_name='hardware_models', on_delete=models.DO_NOTHING)
    set = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Hardware'


class HardwareModel(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    version = models.ForeignKey('Version', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Hardware Models'


class Version(models.Model):
    name = models.CharField(max_length=255)
    major = models.IntegerField(default=1)
    minor = models.IntegerField(default=0)
    patch = models.IntegerField(default=0)

    def __str__(self):
        return f"Version {self.major}.{self.minor}.{self.patch} - {self.name}"


class Order(models.Model):
    number = models.IntegerField(unique=True)
    hardware = models.ForeignKey('Hardware', related_name='orders', on_delete=models.CASCADE)
    order_type = models.CharField(max_length=255)
