# Generated by Django 5.0.4 on 2024-04-20 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_alter_productionstep_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionstep',
            name='production_step_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='production_steps', to='production.productionstepmodel'),
        ),
    ]
