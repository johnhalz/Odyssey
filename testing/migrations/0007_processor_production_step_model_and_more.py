# Generated by Django 5.0.4 on 2024-04-21 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0007_alter_productionstepmodel_step_number'),
        ('testing', '0006_remove_specification_production_step_and_more'),
        ('values_and_units', '0008_unit_create_ts_value_create_ts'),
    ]

    operations = [
        migrations.AddField(
            model_name='processor',
            name='production_step_model',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='processors', to='production.productionstepmodel'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='applicable_scope',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='scoped_specifications', to='values_and_units.range'),
        ),
    ]