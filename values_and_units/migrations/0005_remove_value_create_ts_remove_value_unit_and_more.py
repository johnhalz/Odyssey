# Generated by Django 5.0.4 on 2024-04-20 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('values_and_units', '0004_array_create_ts_decimal_create_ts_integer_create_ts_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='value',
            name='create_ts',
        ),
        migrations.RemoveField(
            model_name='value',
            name='unit',
        ),
        migrations.AlterField(
            model_name='value',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
