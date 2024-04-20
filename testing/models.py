from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Measurement(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    value = models.ForeignKey('values_and_units.Value', related_name='measurements', on_delete=models.CASCADE, null=True, blank=True)
    create_ts = models.DateTimeField(default=timezone.now)
    production_step = models.ForeignKey('production.ProductionStep', related_name='measurements', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.value}"


class SpecificationGroup(models.Model):
    name = models.CharField(max_length=100)
    commencement_date = models.DateField(default=None, null=True, blank=True)
    expiration_date = models.DateField(default=None, null=True, blank=True)
    create_ts = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Specification Group'
        verbose_name_plural = 'Specification Groups'


class Specification(models.Model):
    name = models.CharField(max_length=100)
    valid_range = models.ForeignKey('values_and_units.Range', related_name='validating_specifications', on_delete=models.DO_NOTHING)
    applicable_scope = models.ForeignKey('values_and_units.Range', related_name='scoped_specifications', on_delete=models.DO_NOTHING)
    hardware_model = models.ForeignKey('hardware.HardwareModel', related_name='specifications', on_delete=models.DO_NOTHING)
    production_step_model = models.ForeignKey('production.ProductionStepModel', related_name='specifications', on_delete=models.DO_NOTHING, default=None)
    group = models.ForeignKey('SpecificationGroup', related_name='specifications', on_delete=models.CASCADE)
    description = models.TextField(default=None, null=True, blank=True)
    severity = models.CharField(max_length=100)
    version = models.ForeignKey('values_and_units.Version', related_name='specifications', on_delete=models.DO_NOTHING)
    create_ts = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Result(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    create_ts = models.DateTimeField(default=timezone.now)
    measurements = models.ManyToManyField('Measurement', related_name='results', blank=True)
    specification = models.ForeignKey('Specification', related_name='results', blank=True, on_delete=models.DO_NOTHING, null=True, default=None)
    value = models.ForeignKey('values_and_units.Value', related_name='results', on_delete=models.CASCADE, null=True, blank=True, default=None)
    processor = models.ForeignKey('Processor', related_name='results', on_delete=models.DO_NOTHING, null=True, blank=True, default=None)


class NonCompliance(models.Model):
    result = models.ForeignKey('Result', related_name='non_compliances', on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    decision = models.TextField(default=None, null=True, blank=True)
    reporter = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='reported_non_compliances')
    signer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='signed_non_compliances', null=True, blank=True, default=None)
    create_ts = models.DateTimeField(default=timezone.now)
    close_ts = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Non-Compliance'
        verbose_name_plural = 'Non-Compliances'


class NonComplianceComment(models.Model):
    parent = models.ForeignKey('self', related_name='sub_comments', on_delete=models.CASCADE, null=True, blank=True)
    non_compliance = models.ForeignKey(NonCompliance, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='non_compliance_comments', null=True, blank=True)
    content = models.TextField(default=None, null=True, blank=True)
    create_ts = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Non-Compliance Comment'
        verbose_name_plural = 'Non-Compliance Comments'


class Processor(models.Model):
    name = models.CharField(max_length=100)
    create_ts = models.DateTimeField(default=timezone.now)
    version = models.ForeignKey('values_and_units.Version', related_name='processors', on_delete=models.CASCADE)
    file_path = models.FilePathField(path='.', recursive=True)

    def __str__(self):
        return self.name
