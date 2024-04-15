# Generated by Django 5.0.4 on 2024-04-15 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odyssey_production', '0007_unit_plural_name_unit_space_after_value_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('major', models.IntegerField(default=1)),
                ('minor', models.IntegerField(default=0)),
                ('patch', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HardwareModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='odyssey_production.hardwaremodel')),
                ('version', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='odyssey_production.version')),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=255, unique=True)),
                ('set', models.IntegerField(default=1)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='hardware_models', to='odyssey_production.hardwaremodel')),
            ],
        ),
    ]
