# Generated by Django 5.0.4 on 2024-04-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0004_alter_equipment_parent_alter_hardwaremodel_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='number',
            field=models.PositiveIntegerField(default=1, unique=True),
        ),
    ]
