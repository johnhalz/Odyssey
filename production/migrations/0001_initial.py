# Generated by Django 5.0.4 on 2024-04-16 20:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hardware', '0003_alter_hardwaremodel_version_delete_version'),
        ('values_and_units', '0002_version'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionStepModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('step_number', models.IntegerField(default=0)),
                ('optional', models.BooleanField(default=False)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='production_step_models', to='hardware.equipment')),
                ('hardware_model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='production_step_models', to='hardware.hardwaremodel')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='production.productionstepmodel')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production_step_models', to='values_and_units.version')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('start_timestamp', models.DateTimeField()),
                ('end_timestamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='executed_production_steps', to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='production_steps', to='hardware.order')),
                ('production_step_model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='production_steps', to='production.productionstepmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('hardware_model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='configurations', to='hardware.hardwaremodel')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configurations', to='values_and_units.value')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configurations', to='values_and_units.version')),
                ('production_step_model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='configurations', to='production.productionstepmodel')),
            ],
        ),
    ]
