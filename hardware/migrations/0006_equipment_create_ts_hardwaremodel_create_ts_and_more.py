# Generated by Django 5.0.4 on 2024-04-20 18:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0005_alter_equipment_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='create_ts',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='hardwaremodel',
            name='create_ts',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='order',
            name='create_ts',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
