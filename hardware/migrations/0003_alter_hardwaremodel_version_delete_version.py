# Generated by Django 5.0.4 on 2024-04-16 20:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0002_equipment'),
        ('values_and_units', '0002_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardwaremodel',
            name='version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='values_and_units.version'),
        ),
        migrations.DeleteModel(
            name='Version',
        ),
    ]
